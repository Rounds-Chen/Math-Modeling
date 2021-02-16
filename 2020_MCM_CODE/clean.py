import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.offline as pltoff
from plotly.offline import init_notebook_mode, iplot
import csv
import numpy as np

token='pk.eyJ1IjoiY2hlbnNzc3MiLCJhIjoiY2trdDNqM3l1MGQ0NDMxbXluMDVuYjZqYyJ9.HweaywsB0fvcn80tcAeS2Q'
px.set_mapbox_access_token(token)

# 获取文件所有数据
inpath=r'3.csv'
f=open(inpath,'r')
reader=csv.reader(f)
data=[]
for item in reader:
    data.append(item)
f.close()
# 将两年的数据分开
data_19,data_20=[],[]
for item in data[1:]:
    temp=[]
    for i in item[0:]:
        temp.append(float(i))
    if float(item[0])>100:
            data_20.append(temp)
    else:
            data_19.append(temp)

data_19=np.array(data_19)
data_20=np.array(data_20)
comb_data=np.vstack((data_19,data_20))
#print(comb_data) # 两年的规整数据

places19=pd.DataFrame(data_19,columns=['date','ln','lat'])
places20=pd.DataFrame(data_20,columns=['date','ln','lat'])
places=np.vstack((data_19,data_20))
places=pd.DataFrame(places,columns=['date','ln','lat'])
places['size']=[0.5]*places.shape[0] # 点的大小

#print(places20)
#print(places19)
print(places)
'''''
cln,clat=comb_data[0][1],comb_data[0][2]
arrows=[]
for i in range(len(comb_data)):
    test=dict(
    type='scattergeo',
    lat=[clat, comb_data[i][2]],
    lon=[cln, comb_data[i][1]],
    mode='lines'
    )
    arrows.append(test)

fig=go.Figure(data=arrows)
pltoff.plot(fig,filename='t1.html')
'''''

#绘制热力图
fig=px.scatter_mapbox(places,lat='lat',lon='ln',color='date',
                      size='size',
                      color_continuous_scale=px.colors.sequential.Agsunset,
                      center={'lat':48.95559,'lon':-122.661},
                      #mapbox_style='satellite',
                      width=600,height=500)
pltoff.plot(fig,filename='heatscattermap.html')

'''
# 19和20的数据放在一个图
fig = go.Figure(go.Scattermapbox(mode='markers',
                                 marker={'size':10},
                                 lon = places19.ln,
                                 lat = places19.lat,
                                 #hovertext = places.name,
                                 #hoverinfo = 'text',
                                 )
                )
fig.add_scattermapbox(mode='markers',
                                 lon=places20.ln,
                                 lat=places20.lat,
                                 # hovertext = places.name,
                                 # hoverinfo = 'text',
                                 )
fig.update_layout(
    margin ={'l':0,'t':0,'b':0,'r':0},
    mapbox = {
        #'center': {'lon': places19.ln[0], 'lat': places19.lat[0]},
        'style': "stamen-terrain",
       # 'center': {'lon': places19.ln[0], 'lat': places19.lat[0]},
        'zoom': 1})

iplot(fig)
'''

'''
# 19和20的连线图
import plotly.graph_objects as go

# 单纯画19年的点
fig = go.Figure(go.Scattermapbox(
    mode = "markers",
    lon = places19.ln,
    lat = places19.lat,
    marker = {'size': 10}))

# 给20年的数据加线，中心为c20
c20_ln=places20.ln[0] # 20数据的中心
c20_lat=places20.lat[0]
for i in range(data_20.shape[0]):
    fig.add_trace(go.Scattermapbox(
    line={'color':'red'},
    mode = "markers+lines",
    lon = [places20.ln[i],c20_ln],
    lat = [places20.lat[i],c20_lat],
    marker = {'size': 10}))

fig.update_layout(
    margin ={'l':0,'t':0,'b':0,'r':0},
    mapbox = {
        #'center': {'lon': places19.ln[0], 'lat': places19.lat[0]},
        'style': "stamen-terrain",
        #'center': {'lon': places19.ln[0], 'lat': places19.lat[0]},
        'zoom': 1})


fig.show()
'''