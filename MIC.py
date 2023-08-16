import numpy as np
from minepy import MINE
import xlrd

worksheet = xlrd.open_workbook('G:\python\MIC\测试.xls')
sheet_names= worksheet.sheet_names()
for sheet_name in sheet_names:
    sheet = worksheet.sheet_by_name(sheet_name)

x = sheet.col_values(1) #生成等间隔数，范围0——100，数据个数为1
y = sheet.col_values(2)
mine = MINE(alpha=0.6, c=15)
mine.compute_score(x, y)

print("Without noise:")
print("MIC", mine.mic())
print()

np.random.seed(0)
y += np.random.uniform(-1, 1, x.shape[0])  # add some noise
mine.compute_score(x, y)

print("With noise:")
print("MIC", mine.mic())
#原文链接：https://blog.csdn.net/FontThrone/article/details/85227239