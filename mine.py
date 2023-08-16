import numpy as np
import pandas as pd
from mine import MINE

inpath = r'G:\测试.xlsx'
outpath = r'G:\abc-MIC系数.xlsx'
data_df = pd.read_excel(inpath)

depend_names = ['A', 'B','C'] #depend_name=因变量所在列名，indep_names 自变量所在列，列名的列表
output_mic = pd.DataFrame(columns=['变量1', '变量2', 'MIC系数'])

for var1 in depend_names:
    for var2 in depend_names:
        x = data_df[var1]
        y = data_df[var2]
        mine = MINE(alpha=0.6, c=15)
        mine.compute_score(x, y)
        print(mine.mic())
    out_dict = {'变量1': var1,'变量2': var2,'MIC系数': mine.mic()}
    output_mic = output_mic.append(out_dict, ignore_index=True)

output_mic.to_excel(outpath)
