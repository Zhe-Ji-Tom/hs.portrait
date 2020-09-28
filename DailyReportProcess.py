import pymysql
import sys
from Category import get_tags_by_category

# 数据源地址
url = sys.argv[1]
# 数据源用户名
username = sys.argv[2]
# 数据源密码
password = sys.argv[3]


def analyze():
    # 连接数据库
    connect = pymysql.connect(url, username, password)
    # 获取工作分类及规则
    categories = get_tags_by_category(connect)
    cursor = connect.cursor()
    cursor.execute("SELECT ID FROM USER")
    user_list = cursor.fetchall()
    for user in user_list:
        cursor.execute("SELECT ID, CONTENT FROM DAILY_REPORT WHERE USER_ID = %d ORDER BY TIME DESC LIMIT 1", user)
        daily_report = cursor.fetchone()
        for category in categories.keys():
            tags = categories.get(category)
            for tag in tags:
                if tag in daily_report[1]:
                    cursor.execute("INSERT INTO DAILY_REPORT_RESULT (DAILY_REPORT_ID, CATEGORY) VALUES (%d, %s)",
                                   (daily_report[0], category))
                    connect.commit()
                break





