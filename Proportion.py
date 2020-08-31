import xlrd
import jieba.analyse
from xlutils.copy import copy

coding = ['开发', '优化', '部署', '修复', '发版', '编写', '']
meeting = ['会议', '讨论', '']
learning = ['学习', '知识', '']
solving = ['解决', '测试', '配合', '对接', '协助', '']


def generate_proportion(url):
    # open excel
    excel = xlrd.open_workbook(url, formatting_info=True)
    # choose sheet of weekly reports
    read_sheet = excel.sheet_by_index(1)
    workbook = copy(excel)
    write_sheet = workbook.get_sheet(1)

