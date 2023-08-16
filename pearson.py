import xlrd
import numpy as np
import pandas as pd
from scipy import stats
from scipy.stats import pearsonr


def read(file):
    wb = xlrd.open_workbook(r'G:\python\Pearson\八年级男生体测数据.xls')
    sheet = wb.sheet_by_index(0)
    rows = sheet.nrows
    all_content = []
    for j in range(0, 6):
        temp = []
        for i in range(1,rows) :
            cell = sheet.cell_value(i, j)
            temp.append(cell)
        all_content.append(temp)
        temp = []
    return np.array(all_content)


def calculate(datas):
    MIN = np.min(datas,axis = 1)
    MAX = np.max(datas,axis = 1)
    AVG = np.average(datas,axis = 1)
    MEDIAN = np.median(datas,axis = 1)
    SKEWNESS =stats.skew(datas,axis = 1)
    KURTOSIS = stats.kurtosis(datas,axis = 1)
    STD = np.std(datas,axis = 1)
    result = np.array([MIN,MAX,AVG,MEDIAN,SKEWNESS,KURTOSIS,STD])
    return result


def write(answer_data):
    writer = pd.ExcelWriter('G:\python\Pearson\A.xlsx')
    answer_data.to_excel(writer, 'page_1', float_format='%.5f')
    writer.save()
    writer.close()

datas=read('G:\python\Pearson\八年级男生体测数据.xls')
result = calculate(datas)   #统计描述
corrcoe = np.corrcoef(result)   #计算皮尔逊相关系数
answer_data = pd.DataFrame(result)        #将ndarry转换为DataFrame
write(answer_data)