import pandas as pd
import numpy as np

path="C:\\Users\\round\\Desktop\\test.xlsx" # 数据所存储的xlsx文件
rh,ch=1,1 #读取表格的起始行和列
def readData(table,rh,ch):
    df=pd.read_excel(table) #读取名为table的表格的xxx表单
    nrows=df.shape[0] #表格总行数
    ncols=df.shape[1] #表格总列数
    data=df.iloc[df.rows[rh:nrows],df.columns[ch:ncols]]
    return np.array(data)

def entropy(data):
    mins=data.min(axis=1) #data中每列的最小值
    maxs=data.max(axis=1) #data中每列的最大值

data=readData(path,rh,ch)
print(data)