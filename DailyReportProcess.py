import pymysql
import xlrd
import sys
from Category import get_tags_by_category

# excel文件地址
excel_url = sys.argv[1]


def analyze():
    # 打开日志excel文件
    excel = xlrd.open_workbook(excel_url, formatting_info=True)
    # 选择日报表单
    read_sheet = excel.sheet_by_index(0)
    # 获取总行数
    rows = read_sheet.nrows
    # 获取工作分类及规则
    categories = get_tags_by_category()
    # 连接数据库
    connect = pymysql.connect('localhost', user='root', passwd='root', db='test')
    cursor = connect.cursor()

    for i in rows:
        # 获取日报内容
        content = read_sheet.cell_value(i, 5)
        for category in categories.keys():
            tags = categories.get(category)
            for tag in tags:
                if tag in content:
                    # TODO 日志ID
                    cursor.execute("INSERT INTO DAILY_REPORT_RESULT (DAILY_REPORT_ID, CATEGORY) VALUES (%d, %d)",
                                   ("", category))
                break




