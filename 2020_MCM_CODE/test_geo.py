from math import *

def geo_dis(lng1,lat1,lng2,lat2):
   # lng1,lat1,lng2,lat2=[lng1,lat1,lng2,lat2]*math.pi/180.0

    dlng=(lng2-lng1)*pi/180.0
    dlat=(lat2-lat1)*pi/180.0
    a=sin(dlat/2)**2+cos(lat1)*cos(lat2)*sin(dlng/2)**2
    c=2*asin(sqrt(a))
    r=6371

    dis=c*r #单位km
    return dis

earth_arc,earth_radis=111.199,6378.137 # 地每度的弧长，赤道半径
def getGeoPos(dis,azimuth,lon0,lat0): # 根据方位角和距离计算经纬度
    #azimuth=radians(azimuth)
    lon=lon0+(dis*sin(azimuth))/(earth_arc*cos(radians(lat0)))
    lat=lat0+(dis*cos(azimuth))/earth_arc
    return [lon,lat]

ln1,lat1=-122.7255848,48.9931665 # 起始点
dis=40
lonl,latl=getGeoPos(dis,1.5*pi,ln1,lat1) # 左点
lonu,latu=getGeoPos(dis,0,ln1,lat1) #上点
lonr,latr=getGeoPos(dis,0.5*pi,ln1,lat1) #右点
lonb,latb=getGeoPos(dis,pi,ln1,lat1) #下点

lon1,lon2=lonl,lonr #左右经度范围
lat1,lat2=latu,latb #上下纬度范围

print(lon1,lon2,lat1,lat2)