import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.offline import init_notebook_mode, iplot
import plotly.offline as pltoff
import seaborn as sns


def Draw0(list,shape,scale):
    fig=plt.figure()

    ax1=fig.add_subplot(111)
    x=np.random.gamma(shape,scale,10000)
    sns.kdeplot(x,legend=True,label='shape='+str(shape)+' '+'scale='+str(scale),color='#48D1CC',ax=ax1)



    plt.tick_params(axis='x',
                    which='both',

                    labelsize=10,
                    labelcolor='#4d4f53',
                    labelleft='off',
                    labelbottom='off')
    plt.tick_params(axis='y',
                    which='both',
                    pad=10,

                    labelsize=10,
                    labelcolor='#4d4f53',
                    labelleft='off',
                    labelbottom='off')
    plt.legend(loc = 'best')


    ax2=ax1.twinx()
    ax2.set_ylim(0,0.25)
    ax2.set_ylabel('Frequency')
    ax2.bar(list,[0.2]*len(list),width=0.2,color= '#87CEFA')

    ax = plt.gca()
    ax.spines['top'].set_visible(False)  # 关闭上坐标轴
    x_0=np.arange(0,40)


    plt.show()

list=[1.8011 ,   2.4841 ,   4.6634  ,  0.7684 ,   0.1568,    0.4181,    0.1565 ,   0.1498 ,   0.1539]
shape,scale= 0.7507 ,   1.5914
Draw0(list,shape,scale)




def Draw1(data):
    #show_data=data[['Lab Status','RSR_Rank']]
    #show_data=show_data.rename_axis('Pos')
    #show_data.to_csv('final_data_show_1.csv')
    plt.gca().margins(x=0)
    plt.gcf().canvas.draw()
    tl = plt.gca().get_xticklabels()
    maxsize = max([t.get_window_extent().width for t in tl])
    m = 0.2  # inch margin
    s = maxsize / plt.gcf().dpi * 5000 + 2 * m
    margin = m / plt.gcf().get_size_inches()[0]

    plt.gcf().subplots_adjust(left=margin, right=1. - margin)
    plt.gcf().set_size_inches(s, plt.gcf().get_size_inches()[1])

    #plt.xticks(np.arrange(0,5000,step=1000))
    #plt.plot(data.Pos,data.RSR_Rank,'r-o')
    n=data.shape[0]
    for i in range(n):
        if data.iloc[i][1]=='Positive ID':
            c='#FF0000'
        elif data.iloc[i][1]=='Negative ID':
            c='#E6E6FA'
        elif data.iloc[i][1]=='Unverified':
            c='#FDF5E6'
        else:
            c='#E0FFFF'
        plt.axvline(data.iloc[i][0],ymax=data.iloc[i][2]/max(data.RSR_Rank),color=c)
    plt.axvline(0,ymax=0,color='#FF0000',label='Positive ID')
    plt.axvline(0,ymax=0,color='#E6E6FA',label='Negative ID')
    plt.axvline(0,ymax=0,color='#FDF5E6',label='Unverified')
    plt.axvline(0,ymax=0,color='#E0FFFF',label='Unprocessed')

    ax = plt.gca()
    ax.spines['top'].set_visible(False)  # 关闭上坐标轴
    ax.spines['right'].set_visible(False)  # 关闭上坐标轴

    plt.xlabel('Priority')
    plt.ylabel('WRSR Rank')
    plt.yticks([])

    plt.tick_params(axis='x',
                    which='both',

                    labelsize=10,
                    labelcolor='#4d4f53',
                    labelleft='off',
                    labelbottom='off')
    plt.tick_params(axis='y',
                    which='both',
                    pad=10,

                    labelsize=10,
                    labelcolor='#4d4f53',
                    labelleft='off',
                    labelbottom='off')
    plt.legend(loc = 'best')

    plt.show()

'''
plt.plot([1,2,3])
plt.yticks([])
plt.show()
'''
token='pk.eyJ1IjoiY2hlbnNzc3MiLCJhIjoiY2trdDNqM3l1MGQ0NDMxbXluMDVuYjZqYyJ9.HweaywsB0fvcn80tcAeS2Q'
px.set_mapbox_access_token(token)

def Draw2(data):
    fig = px.scatter_mapbox(data, lat='Latitude', lon='Longitude', color='Priority',
                            #size='size',
                            color_continuous_scale=px.colors.sequential.solar,
                            center={'lat': 48.95559, 'lon': -122.661},
                            # mapbox_style='satellite',
                            width=1000, height=800,
                            #size=[0.5]*data.shape[0]
                            )
    #pltoff.plot(fig, filename='figure6.html')
    iplot(fig)
''''
file=r'forecast_data_to_map.CSV'
data=open(file,'r')
data=pd.read_csv(data)
data=data[data['Lab Status'].isin(['Unverified','Unprocessed'])][['Latitude','Longitude','Priority']]
Draw2(data)
'''

def Draw3(p1,p2,p3,p4,p5,p6):
    fig = px.scatter_mapbox(width=600,height=400,
                                     lon=p1.lon,
                                     lat=p1.lat,
                            size=[1]*p1.shape[0]
                                     )


    fig.add_scattermapbox(mode='markers',

                          lon=p2.lon,
                          lat=p2.lat
                          )
    fig.add_scattermapbox(mode='markers',
                          lon=p3.lon,
                          lat=p3.lat
                          )
    fig.add_scattermapbox(mode='markers',
                          lon=p4.lon,
                          lat=p4.lat
                          )
    fig.add_scattermapbox(mode='markers',
                          lon=p5.lon,
                          lat=p5.lat
                          )
    fig.add_scattermapbox(mode='markers',
                          lon=p6.lon,
                          lat=p6.lat
                          )


    fig.update_layout(
        margin={'l': 0, 't': 0, 'b': 0, 'r': 0},
        mapbox={
            # 'center': {'lon': places19.ln[0], 'lat': places19.lat[0]},
            #'style': "basic",
            # 'center': {'lon': places19.ln[0], 'lat': places19.lat[0]},
            'zoom': 1}
    )

    pltoff.plot(fig, filename='figure7.html')
    #iplot(fig)
'''''
if __name__=='__main__':
    p1=pd.DataFrame({
        'lon':[-122.688503,-122.700941,-122.810653,-122.702242],
        'lat':[48.980994,48.971949,49.025831,48.993892]
    })
    p2=pd.DataFrame({
        'lon':[-122.574809,-122.581335,-122.582465,-122.57472,-122.574726],
        'lat':[48.984269 ,48.979497,48.983375,48.984172,48.98422  ]
    })
    p3=pd.DataFrame({
        'lon':[-122.661037],
        'lat':[48.955587]
    })
    p4=pd.DataFrame({
        'lon':[-122.641648],
        'lat':[49.060215]
    })
    p5=pd.DataFrame({
        'lon':[-122.418612],
        'lat':[48.777534]
    })
    p6=pd.DataFrame({
        'lat':[48.927519],
        'lon':[-122.745016]
    })
    print(p1)
    Draw3(p1,p2,p3,p4,p5,p6)
'''
