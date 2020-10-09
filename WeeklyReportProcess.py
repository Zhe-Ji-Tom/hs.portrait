import jieba.analyse
import sys
import pymysql

# 数据源地址
url = sys.argv[1]
# 数据库名称
datasource_name = sys.argv[2]
# 数据源用户名
username = sys.argv[3]
# 数据源密码
password = sys.argv[4]
# 词云时间周期
period = int(sys.argv[5])
# 选取高频词数量
top = int(sys.argv[6])


def analyze():
    try:
        # 连接数据库
        connect = pymysql.connect(url, username, password, datasource_name)
    except Exception:
        print("数据库连接失败！请检查数据库配置。")
        return
    cursor = connect.cursor()
    cursor.execute("SELECT ID FROM USER")
    user_list = cursor.fetchall()
    for user in user_list:
        print("计算用户ID为{" + str(user[0]) + "}的词云")
        # 从数据库读取周报
        cursor.execute("SELECT ID,CONTENT FROM WEEKLY_REPORT WHERE USER_ID = %s ORDER BY REPORT_TIME DESC LIMIT %s", (user[0], period))
        weekly_report_list = cursor.fetchall()
        if weekly_report_list :
            weekly_report_set = ""
            for i in range(len(weekly_report_list)):
                weekly_report_set = weekly_report_set + weekly_report_list[i][1]
            # 计算词云
            tfidf = jieba.analyse.tfidf(weekly_report_set, topK=top, withWeight=False, allowPOS='n')
            # 结果写入数据库
            cursor.execute("UPDATE WEEKLY_REPORT SET WORD_CLOUD = %s WHERE ID = %d", (tfidf, weekly_report_list[0][0]))
            connect.commit()


analyze()
