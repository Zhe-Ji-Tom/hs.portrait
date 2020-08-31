import xlrd
import jieba.analyse
import xlwt
import xlutils
from xlutils.copy import copy
from WordCloud import generate_word_cloud

generate_word_cloud("20200713163155845.xls", 20)
#
# excel = xlrd.open_workbook("20200713163155845.xls")
# sheets = excel.sheet_names()
# workSheet = excel.sheet_by_index(1)
#
# cell = workSheet.cell_value(2,5)
# text = workSheet.col_values(5)
#
# text = "".join(text)
#
# # print(sheets)
# print(cell)
# #
# # textRank = jieba.analyse.textrank(text, topK=10, withWeight=True, allowPOS='v')
# tfidf = jieba.analyse.tfidf(cell, topK=5, withWeight=True, allowPOS='n')
# # #
# # # print(textRank)
# # #
# print(tfidf)

# result = ''
# for i in tfidf:
#     result = result + i[0] + ','
# print(result)


# rb = xlrd.open_workbook("20200713163155845.xls", formatting_info=True)
# r_sheet = rb.sheet_by_index(1)
# wb = copy(rb)
# w_sheet = wb.get_sheet(1)
# w_sheet.write(2, 17, 'test')
# wb.save("20200713163155845.xls")



