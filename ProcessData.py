import xlrd
import jieba.analyse
import xlwt
import xlutils
from xlutils.copy import copy
from WordCloud import generate_word_cloud
import re

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

# split string
# split by '.'
sentences = re.split(r'([0-9]?[0-9]\.)', cel_b2)
model = 1
# split by '、'
if len(sentences) == 1:
    sentences = re.split(r'([0-9]?[0-9]、)', cel_b2)
    model = 2
if len(sentences) == 1:
    model = 0

# remove meaningless sentences
if model != 0:
    for sen in sentences:
        if sen == '':
            sentences.remove(sen)
    for sen in sentences:
        if model == 1:
            if "." in sen:
                sentences.remove(sen)
        else :
            if "、" in sen:
                sentences.remove(sen)
print(sentences)

for sen in sentences:
    tags_pairs_TFIDF = jieba.analyse.extract_tags(sen, topK=5, withWeight=True, allowPOS=('v'))
    print(tags_pairs_TFIDF)

