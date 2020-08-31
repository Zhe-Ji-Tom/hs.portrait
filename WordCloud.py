import xlrd
import jieba.analyse
from xlutils.copy import copy


def generate_word_cloud(url, top):
    # open excel
    excel = xlrd.open_workbook(url, formatting_info=True)
    # choose sheet of weekly reports
    read_sheet = excel.sheet_by_index(1)
    workbook = copy(excel)
    write_sheet = workbook.get_sheet(1)

    row = read_sheet.nrows

    for i in range(row):
        cell = read_sheet.cell_value(i, 5)
        tfidf = jieba.analyse.tfidf(cell, topK=top, withWeight=True, allowPOS={'n'})
        # pick keyword
        result = ''
        for arr in tfidf:
            result = result + arr[0] + ','

        write_sheet.write(i, 17, result)

    workbook.save(url)
