import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib import cm
import pandas as pd

# 获得坐标概率表
def getGeoProbsList(filename):
    GM=np.loadtxt(filename)
    n=5000000
    #求概率质量函数矩阵
    mass=[]
    for gm in GM:
        a=gm/n
        mass.append(a)
    #归一化矩阵，约为每点出现蜜蜂的概率
    normal=[]
    max_mass=0
    for m in mass:
        if max(m)>max_mass:
            max_mass=max(m)
    for m in mass:
        b=m/max_mass #每点的概率值
        normal.append(b)

    return normal

normal_19=getGeoProbsList('GM_19.txt')
normal_20=getGeoProbsList('GM.txt')
# 计算每个小格子概率
def getGeoProb(lon,lat,year):
    lon_l, lat_u = -123.27380699518947, 49.352881965067134  # 区域左边经度，上边纬度
    w, h = (-122.17736260481051 + 123.27380699518947) / 1000, (-48.63345103493287 + 49.352881965067134) / 1000

    index_x, index_y = math.floor((lon - lon_l) / w), math.floor((-lat + lat_u) / h)
    if index_x<0 or index_x>=1000 or index_y<0 or index_y>=1000:
        return 0
    else:
        if year=='2019':
            normal=normal_19
        else:
            normal=normal_20
        return normal[index_y][index_x]

def getGeoProbsList(data):
    #Result=pd.DataFrame()
    data['GeoProb']=data.apply(lambda row:getGeoProb(row['Longitude'],row['Latitude'],row['Year']),axis=1)
    return data

# 获取日期的year，month信息
def getYear(date):
        year,month,day=date.split('/')
        return year
def getMonth(date):
    year, month, day = date.split('/')
    return month
# 添加时间信息
def AddDateMes(data):
    data['Year']=data.apply(lambda row:getYear(row['Detection Date']),axis=1)
    data['Month'] = data.apply(lambda row: getMonth(row['Detection Date']), axis=1)
    return data

# 获取日期对应值
month_value={'1':0,'2':0,'3':0,'4':0,'5':0.5,'6':1.5,'7':3,'8':4.5,'9':5,'10':4,'11':2,'12':0}
def getDateValue(year,month):
    if year==2019 or year==2020:
        return month_value[str(month)]
    else:
        return 0

def getDatesList(data):
    #Result = pd.DataFrame()
    #data=pd.read_csv(Result)
    data['DateValue']=data.apply(lambda row:getDateValue(row['Year'],row['Month']),axis=1)
    return data

# 获取图像对应数据
def getImageValuesList(data,fileBName):
    dataB=open(fileBName,'r',encoding='utf-8-sig') # ID-Image数据
    dataB=pd.read_csv(dataB)
    #dataB=dataB.groupby(by='GlobalID')['ImageProb'].mean() # 相同ID根据ImageProb求均值合并
    idB=dataB.columns.get_loc('GlobalID')
    valB=dataB.columns.get_loc('ImageProb')
    data['ImageProb'] = 0 # data新增一列
    col=data.columns.get_loc('ImageProb') # 获取该列列号
    numB = dataB.shape[0]
    for i in range(numB):
        id, value = dataB.iloc[i][idB], dataB.iloc[i][valB]  # 获取每行id,value

        row = data[data['GlobalID'].isin([id])].index
        index = row[0]
        data.iloc[index,col] = value
    return data


if __name__=='__main__':
    filename=r'temp.csv'
    f=open(filename,'r',encoding='utf-8-sig')
    data=pd.read_csv(f)

    #data=AddDateMes(data)
    #data.to_csv('2021MCMProblemC_DataSet_2.csv',encoding='utf-8-sig') # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!总结这个编码问题

    #Result=pd.DataFrame()
    #data=getGeoProbsList(data)# 获取位置坐标概率项->返回df类型
    #data=getDatesList(data) # 获取时间项->返回df类型
    filename=r'image-prob.csv' # 存储ID-Image-Value的文件
    data=getImageValuesList(data,filename)
    data.to_csv('temp.csv',encoding='utf-8-sig',index=False)

    final_data=data[['Lab Status','GeoProb','DateValue','ImageProb']] # 存储所有信息用于训练的文件
    final_data.to_csv('final_data.csv',encoding='utf-8-sig',index=False)

    #forecast_data=data[data['Lab Status'].isin(['Unverified','Unprocessed'])][['GlobalID','GeoProb','DateValue','ImageProb']] # 存储待预测的数据
    #forecast_data.to_csv('forecast_data.csv',encoding='utf-8-sig',index=False)
    #result.to_csv('Samples.csv') # 将获得的每个样本的指标写入文件
