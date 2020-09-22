import xlrd
import jieba.analyse
import sys
import pymysql
import time

# excel文件地址
excel_url = sys.argv[1]
# 词云时间周期
period = int(sys.argv[2])
# 选取高频词数量
top = int(sys.argv[3])


def analyze():
    # 打开日志excel文件
    excel = xlrd.open_workbook(excel_url, formatting_info=True)
    # 选择周报表单
    read_sheet = excel.sheet_by_index(1)
    # 获取总行数
    rows = read_sheet.nrows
    # 连接数据库
    connect = pymysql.connect('localhost', user='root', passwd='root', db='test')
    cursor = connect.cursor()
    for i in rows:
        # 获取周报内容
        content = read_sheet.cell_value(i, 5)
        # 获取工号
        user_id = read_sheet.cell_value(i, 0)
        # 从数据库读取之前周报
        cursor.execute("SELECT CONTENT FROM WEEKLY_REPORT WHERE USER_ID = %d", (period-1))
        previous_weekly_report = cursor.fetchall()
        weekly_report_set = content
        for report in previous_weekly_report:
            weekly_report_set = weekly_report_set + report
        # 获取周报日期
        string_time = read_sheet.cell_value(i, 4)
        date_time = time.strftime('%Y-%m-%d %H:%M', string_time)
        # 计算词云
        tfidf = jieba.analyse.tfidf(weekly_report_set, topK=top, withWeight=False, allowPOS='n')
        # 结果写入数据库
        cursor.execute("INSERT INTO WEEKLY_REPORT (CONTENT, TIME, WORD_CLOUD) VALUES (%s, %d, %s)",
                       (content, date_time, tfidf))
        connect.commit()
