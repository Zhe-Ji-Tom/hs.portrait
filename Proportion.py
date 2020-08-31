import xlrd
import jieba.analyse
from xlutils.copy import copy


def generate_proportion(url):
    # open excel
    excel = xlrd.open_workbook(url, formatting_info=True)
    # choose sheet of weekly reports
    read_sheet = excel.sheet_by_index(1)
    workbook = copy(excel)
    write_sheet = workbook.get_sheet(1)

