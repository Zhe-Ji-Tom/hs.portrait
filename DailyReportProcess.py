import pymysql
import sys
from Category import get_keywords_by_label

# 数据源地址
url = sys.argv[1]
# 数据库名称
datasource_name = sys.argv[2]
# 数据源用户名
username = sys.argv[3]
# 数据源密码
password = sys.argv[4]


def analyze():
    try:
        # 连接数据库
        connect = pymysql.connect(url, username, password, datasource_name)
    except Exception:
        print("数据库连接失败！请检查数据库配置。")
        return
    # 获取工作分类及规则
    keywords_map = get_keywords_by_label(connect)
    cursor = connect.cursor()
    cursor.execute("SELECT ID FROM USER")
    user_list = cursor.fetchall()
    for user in user_list:
        print("计算用户ID为{" + str(user[0]) + "}的词云")
        # 读取日报ID及内容
        cursor.execute("SELECT ID, CONTENT FROM DAILY_REPORT WHERE USER_ID = %s ORDER BY REPORT_TIME DESC LIMIT 1", user[0])
        daily_report = cursor.fetchone()
        for label in keywords_map.keys():
            keywords = keywords_map.get(label)
            for keyword in keywords:
                if keyword in daily_report[1]:
                    # 记录日报工作类型
                    cursor.execute("SELECT ID FROM KEYWORDS WHERE KEYWORD = %s", keyword)
                    keyword_id = cursor.fetchone()
                    cursor.execute("INSERT INTO DAILY_REPORT_RESULT (DAILY_REPORT_ID, KEYWORD_ID) VALUES (%d, %d)",
                                   (daily_report[0], keyword_id))
                    connect.commit()
                break





