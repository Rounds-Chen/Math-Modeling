import pandas as pd
import  numpy as np
from math import *


data=pd.read_csv(r'GM.txt',sep=' ',header=None)
numSlices=1000
lon_l,lat_u=-123.27380699518947,49.352881965067134 # 区域左边经度，上边纬度
w,h=(-122.17736260481051+123.27380699518947)/numSlices,(-48.63345103493287+49.352881965067134 )/numSlices # 每个格子的宽，高
def getProb(lon,lat):
    index_y, index_x = floor((lon - lon_l) / w), floor((-lat + lat_u) / h)
    return data.iloc[index_x,index_y]


lon,lat=[-122.6610,-122.6416,-122.4186,-122.7450,-122.5748,-122.5813,-122.5825,-122.5747,-122.5747],[48.9556 ,49.0602 ,48.7775,48.9275 ,48.9843 ,48.9795,48.9834 ,48.9842 ,48.9842 ]

for ln,lt in zip(lon,lat):
    print(getProb(ln,lt))