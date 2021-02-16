import pandas as pd

'''
infile=r'test.csv'
data=open(infile,'r',encoding='utf-8-sig')
data=pd.read_csv(data)


data=data.groupby('GlobalID')['ImageProb'].mean()
data.to_csv('testGroupBy.csv',encoding='utf-8-sig')
'''
'''''
fileA=r'2021MCMProblemC_DataSet_1.csv'
fileB=r'testGroupBy.csv'
dataA=open(fileA,'r') # 读取时不能写utf-8-sig编码
dataB=open(fileB,'r')
dataA=pd.read_csv(dataA)
dataB=pd.read_csv(dataB)

dataA['ImageProb']=0
numB=dataB.shape[0]
for i in range(numB):
    id,value=dataB.iloc[i][0],dataB.iloc[i][1] # 获取每行id,value

    row=dataA[dataA['GlobalID'].isin([id])].index
    index=row[0]
    dataA.iloc[index,8]=value
   # dataA.ImageProb[index[0]]=value # 找到该id在A中的位置并替换相应的值
dataA.to_csv('2021MCMProblemC_DataSet_4.csv',encoding='utf-8-sig')
'''
fileB=r'image-prob.csv'
dataB=open(fileB,'r')
dataB=pd.read_csv(dataB)
dataB=dataB.groupby(by='GlobalID')['ImageProb'].mean()
dataB.to_csv('image-prob.csv',encoding='utf-8-sig')