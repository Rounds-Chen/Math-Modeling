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
def new_colony(n):
    angle = np.random.rand(n) * 2 * np.pi
    shape, scale = 2.5090, 3.9410
    length = np.random.gamma(shape, scale, n)
    return angle, length

''''
##模拟2019##
n = int(np.random.normal(1000, 300))  # 产生新的种群数量
a, l = new_colony(n)

# 角度angle、极径length转化成经纬度
location_1 = []  # 新巢穴的经纬度
for a, l in zip(a, l):
    loc = tran(a, l)
    location_1.append(loc)

# 画图
for loc in location_1:
    plot(loc[0], loc[1])

##模拟2020##

'''

# forecast
# centers[0]->lon,centers[1]->lat
def forecast(centers):
    newGeos=[] # 新种群的经纬度
    n = 10  # 产生新的种群数量
    angs,ds=new_colony(n) # 新种群的方位角和距离
    for c in centers:
        for a,l in zip(angs,ds):
            r=np.random.gamma(2,1) # 半径大小
            #print(r)
            temp=getGeoPos(l,a,c[0],c[1])
            temp.append(r)
            newGeos.append(temp)

    return newGeos

# 绘制散点(气泡)地图
def DrawMapScatter(places):
    fig = go.Figure(go.Scattermapbox(mode='markers',
                                     marker={'size': places.radius*10},
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
    pltoff.plot(fig, filename='test.html')

# 绘制气泡地图
def DrawMapBubble(places):
    fig=go.Figure()
    fig.add_trace(go.Scattergeo(
        locationmode='USA-states',
        lon=places.lon,
        lat=places.lat,
        marker=dict(
            size=places.radius,
            sizemode='area'
        )
    ))
    fig.update_layout(
        mapbox={
            'style': "stamen-terrain",
            'zoom':2
        }
    )
    pltoff.plot(fig,filename='bubblemap.html')

'''''
# forecast 2019
lon0,lat0=-122.7255848,48.9931665
centers=[]
centers.append([lon0,lat0])
print(centers)
geo19=forecast(centers)
print(len(geo19))
geo19=np.array(geo19)
geo19=pd.DataFrame(geo19,columns=['lon','lat','radius'])
#geo19.to_csv('4.csv')
print(geo19.radius)
DrawMapScatter(geo19)

'''

