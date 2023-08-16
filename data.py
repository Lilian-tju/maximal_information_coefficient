from mine import MINE
import xlrd
worksheet = xlrd.open_workbook('G:\python\MIC\测试.xls')
sheet_names= worksheet.sheet_names()
print(sheet_names)
for sheet_name in sheet_names:
    sheet = worksheet.sheet_by_name(sheet_name)
    x = sheet.col_values(2) # 获取第二列内容， 数据格式为此数据的原有格式（原：字符串，读取：字符串；  原：浮点数， 读取：浮点数）
    y = sheet.col_values(3)
    print(x)
    print(y)
    mine = MINE(alpha=0.6, c=15)
    mine.compute_score(x, y)
print("MIC", mine.mic())

