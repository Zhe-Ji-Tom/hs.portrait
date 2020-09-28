import jieba.analyse
import sys
import pymysql

# 数据源地址
url = sys.argv[1]
# 数据源用户名
username = sys.argv[2]
# 数据源密码
password = sys.argv[3]
# 词云时间周期
period = int(sys.argv[4])
# 选取高频词数量
top = int(sys.argv[5])


def analyze():
    # 连接数据库
    connect = pymysql.connect(url, username, password)
    cursor = connect.cursor()
    cursor.execute("SELECT ID FROM USER")
    user_list = cursor.fetchall()
    for user in user_list:
        # 从数据库读取周报
        cursor.execute("SELECT ID,CONTENT FROM WEEKLY_REPORT WHERE USER_ID = %d ORDER BY TIME DESC LIMIT %d", (user, period))
        weekly_report_list = [[]]
        weekly_report_list = cursor.fetchall()
        weekly_report_set = ""
        for i in len(weekly_report_list):
            weekly_report_set = weekly_report_set + weekly_report_list[i][1]
        # 计算词云
        tfidf = jieba.analyse.tfidf(weekly_report_set, topK=top, withWeight=False, allowPOS='n')
        # 结果写入数据库
        cursor.execute("UPDATE WEEKLY_REPORT SET WORD_CLOUD = %s WHERE ID = %d", (tfidf, weekly_report_list[0][0]))

    connect.commit()
