from math import *
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.offline as pltoff
import csv

earth_arc,earth_radis=111.199,6378.137 # 地球没度的弧长，赤道半径
def getGeoPos(dis,azimuth,lon0,lat0): # 根据方位角和距离计算经纬度
    #azimuth=radians(azimuth)
    lon=lon0+(dis*sin(azimuth))/(earth_arc*cos(radians(lat0)))
    lat=lat0+(dis*cos(azimuth))/earth_arc
    return [lon,lat]

# 预测新巢的方位角和距离
def new_colony(n,type):
    a,b=0,0
    if type=='colony':
        a=(-1.0/8)
        b=(0.5)
        shape, scale = 2.5090, 3.9410
    else:
        a=0
        b=1
        shape, scale =1.0,0.5
    angle = np.random.uniform(a,b,n) * 2 * np.pi

    length = np.random.gamma(shape, scale, n)
    return angle, length


# forecast
# centers[0]->lon,centers[1]->lat n->新个体数 type->预测种群or个体
def forecast(centers,n,type):
    newGeos=[] # 新个体的经纬度
    angs,ds=new_colony(n,type) # 新种群的方位角和距离
    for c in centers:
        for a,l in zip(angs,ds):
            temp=getGeoPos(l,a,c[0],c[1]) # 新个体的经纬度
            newGeos.append(temp)
    return newGeos


# 绘制散点(气泡)地图
def DrawMapScatter(places):
    fig = go.Figure(go.Scattermapbox(mode='markers',
                                     #marker={'size': places.radius*10},
                                     lon=places.lon,
                                     lat=places.lat,
                                     #hoverinfo='text',
                                     #hovertext = (places.azimuth,places.dis)
                                     )
                    )
    fig.update_layout(
        margin={'l': 0, 't': 0, 'b': 0, 'r': 0},
        mapbox={
            # 'center': {'lon': places19.ln[0], 'lat': places19.lat[0]},
            'style': "stamen-terrain",
            # 'center': {'lon': places19.ln[0], 'lat': places19.lat[0]},
            'zoom': 1})
    pltoff.plot(fig, filename='test1.html')

# Montecarlo
#lon,lat 初始种群的经纬度 k->模拟次数
def MCforecast(lon,lat,k):
    centers = []
    centers.append([lon, lat])
    numCol=10 # 新种群个数
    numBees=500 # 新蜜蜂个数
    numSlices=1000 # 分割数
    GM = np.zeros((numSlices, numSlices),dtype=int)  # 1000*1000的区域
    #GM=np.array(GM)
    #print(GM.shape)
    count,count_w=0,0
    for i in range(k):
        # LDD
        newCols=forecast(centers,numCol,'colony') # 新种群的位置
        # SDD
        lon_l,lat_u=-123.27380699518947,49.352881965067134 # 区域左边经度，上边纬度
        w,h=(-122.17736260481051+123.27380699518947)/numSlices,(-48.63345103493287+49.352881965067134 )/numSlices # 每个格子的宽，高
        newBees = []  # 新个体的经纬度
        angs, ds = new_colony(numBees, 'Bee')  # 新种群的方位角和距离
        for c in newCols:
            for a, l in zip(angs, ds):
                count+=1
                temp = getGeoPos(l, a, c[0], c[1])  # 新个体的经纬度
                #temp=np.array(temp)
                #newBees.append(temp)
                index_y,index_x=floor((temp[0]-lon_l)/w),floor((-temp[1]+lat_u)/h)
                if index_x<0 or index_x>=numSlices or index_y<0 or index_y>=numSlices: #区域外的忽略
                    #print(index_x,index_y)
                    count_w+=1
                #print(index_x,index_y)
                else:
                    GM[index_x][index_y]+=1 # 该区域个数++
    #newBees = pd.DataFrame(newBees, columns=['lon', 'lat'])
    #DrawMapScatter(newBees)
    print(float(count_w)/count)
    np.savetxt('GM.txt',GM) # 将结果保存到GM.txt中

def MCforecast19(lon,lat,k):
    numBees=500 # 新蜜蜂个数
    numSlices=1000 # 分割数
    GM = np.zeros((numSlices, numSlices),dtype=int)  # 1000*1000的区域

    for i in range(k):
        # SDD
        lon_l,lat_u=-123.27380699518947,49.352881965067134 # 区域左边经度，上边纬度
        w,h=(-122.17736260481051+123.27380699518947)/numSlices,(-48.63345103493287+49.352881965067134 )/numSlices # 每个格子的宽，高
        angs, ds = new_colony(numBees, 'Bee')  # 新个体的方位角和距离

        for a, l in zip(angs, ds):
                temp = getGeoPos(l, a, lon, lat)  # 新个体的经纬度
                index_y,index_x=floor((temp[0]-lon_l)/w),floor((-temp[1]+lat_u)/h)
                if index_x<0 or index_x>=numSlices or index_y<0 or index_y>=numSlices: #区域外的忽略
                    pass
                else:
                   GM[index_x][index_y]+=1 # 该区域个数++

    np.savetxt('GM_19.txt',GM) # 将结果保存到GM.txt中

MCforecast19(-122.7255848,48.9931665,100000)
