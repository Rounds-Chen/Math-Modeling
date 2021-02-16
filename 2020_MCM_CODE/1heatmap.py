import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.offline as pltoff
import plotly.express as px
import pandas as df

token = 'pk.eyJ1IjoiY2hlbnNzc3MiLCJhIjoiY2trdDNqM3l1MGQ0NDMxbXluMDVuYjZqYyJ9.HweaywsB0fvcn80tcAeS2Q'
px.set_mapbox_access_token(token)

w, h = (-122.17736260481051 + 123.27380699518947) / 1000, (-48.63345103493287 + 49.352881965067134) / 1000


# convert (x,y) to (lon,lat)
def ConvertToGEO(x, y):
    lon_l, lat_u = -123.27380699518947, 49.352881965067134  # 区域左边经度，上边纬度
    lon = lon_l + y * w
    lat = lat_u - x * h
    return [lon, lat]


def Sum(x, y, data):
    sum = 0.0
    for i in range(-4, 4):
        for j in (-4, 4):
            sum += data.iloc[i + x, j + y]
    return sum


def ConvertFile(file):
    data = df.read_csv(file, sep=' ', header=None)
    print(data.shape)
    arr_data = []
    for i in range(4, 996, 8):
        for j in range(4, 996, 8):
            temp = ConvertToGEO(i, j)  # 每一项
            # print(data.iloc[i,j])
            temp.append(Sum(i, j, data))
            arr_data.append(temp)
    df_data = pd.DataFrame(arr_data, columns=['lon', 'lat', 'size'])
    print(df_data.shape)
    return df_data


# draw scatter map
def DrawMapScatter(places):
    fig = go.Figure(go.Scattermapbox(mode='markers',
                                     # marker={'size': places.radius*10},
                                     lon=places.lon,
                                     lat=places.lat,
                                     # hoverinfo='text',
                                     # hovertext = (places.azimuth,places.dis)
                                     )
                    )
    fig.update_layout(
        margin={'l': 0, 't': 0, 'b': 0, 'r': 0},
        mapbox={
            # 'center': {'lon': places19.ln[0], 'lat': places19.lat[0]},
            # 'style': "stamen-terrain",
            # 'center': {'lon': places19.ln[0], 'lat': places19.lat[0]},
            'zoom': 1})
    pltoff.plot(fig, filename='1_forecast_heatmap.html')

# draw heatmap
def DrawHeatMap(data):
    fig = px.density_mapbox(data, lat='lat', lon='lon', z='size', radius=15,
                            color_continuous_scale=px.colors.sequential.Sunsetdark, height=800, width=1000)
    pltoff.plot(fig, filename='1_forecast_heatmap_19.html')


data = ConvertFile('GM_19.txt')
DrawHeatMap(data)
# print(data)
# DrawMapScatter(data)
'''''
fig=px.scatter_mapbox(data,lat='lat',lon='lon',color='size',
                      color_continuous_scale=px.colors.sequential.Agsunset,
                      center={'lat':48.95559,'lon':-122.661},
                      mapbox_style='satellite',
                      #width=600,height=500)
                      )
pltoff.plot(fig,filename='1_forecast_heatmap.html')
'''
