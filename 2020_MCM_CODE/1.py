import csv
import math
from datetime import datetime
import matplotlib.pyplot as plt
import plotly as py
import plotly.graph_objs as go


# determine the distance based on two latitude and longitude coordinates
def geo_dis(lng1, lat1, lng2, lat2):
    dlng = (lng2 - lng1) * math.pi / 180.0
    dlat = (lat2 - lat1) * math.pi / 180.0
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlng / 2) ** 2
    c = 2 * math.asin(math.sqrt(a))
    r = 6371

    dis = c * r  # km
    return dis


# get the number of days between two dates
# format of t : year/month/day
def times(t, cday):
    y, m, d = t.split('/')
    y, m, d = int(y), int(m), int(d)
    nday = datetime(y, m, d)
    return (nday - cday).days


# tansform one single month into two, eg:1->01
def retype(t):
    y, m = t.split('/')
    if len(m) == 1:
        m = '0' + m
    return y + '/' + m


inpath = r"2021MCMProblemC_DataSet.csv"  # 文件路径
f = open(inpath, 'r')
reader = csv.reader(f)

t0 = '2019/9/30'
y, m, d = t0.split('/')
y, m, d = int(y), int(m), int(d)
cday = datetime(y, m, d)  # 起始日期
pos = []
# 计算每个时间点的距离，输出到 1.csv中
x, y = [], []  # 横坐标为时间间隔，纵坐标为距离
for row in reader:
    if row[3] == 'Positive ID':
        ln2, lat2 = float(row[7]), float(row[6])
        ln1, lat1 = -122.702242, 48.993892  # 起始点
        y.append(geo_dis(ln1, lat1, ln2, lat2))
        x.append(times(row[1], cday))
        pos.append([row[1], geo_dis(ln1, lat1, ln2, lat2), times(row[1], cday)])  # '日期','距离’，‘时间间隔'
f.close()

# 将原始的每个日期的距离数据存储到1.csv
outfile = r"1.csv"  # 输出文件路经
out = open(outfile, 'w', encoding='utf-8', newline='')
writer = csv.writer(out)
writer.writerow(['date', 'dis', 'interval'])
for item in pos:
    writer.writerow([item[0], item[1], item[2]])
out.close()

# 读取最大距离数据供画图
xmax, ymax = [], []  # str类型的时间间隔和距离
f = open('2.csv', 'r')
reader = csv.reader(f)
for row in reader:
    xmax.append(row[2])  # 时间间隔
    ymax.append(row[1])  # 距离

xmax, ymax = xmax[1:], ymax[1:]
xm, ym = [], []  # float类型的时间间隔和类型
for i in xmax:
    xm.append(float(i))
for j in ymax:
    ym.append(float(j))
real_max_y = []
for k in range(len(ymax)):
    if k == 0:
        real_max_y.append(ym[k])
    else:
        real_max_y.append(max(ym[k], real_max_y[k - 1]))
print(real_max_y)

plt.scatter(x, y, marker='*', color='#f48924', s=10)  # draw scatter
plt.plot(xm, real_max_y, color='#0085ad', linestyle='-', markersize=3, linewidth=2)
plt.fill_between(xm[:], real_max_y[:], facecolor='#74d2e7', alpha=0.4)  # fill color between special area
# plt.gcf().autofmt_xdate()  # rotate axis label

ax = plt.gca()
ax.spines['top'].set_visible(False)  # close top-axis
ax.spines['right'].set_visible(False)  # close right-axis
ax.spines['left'].set_visible(False)  # close left-axis
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))

plt.grid(axis='y', )  # open y-axis grid line

plt.xlim(right=400)
plt.xlabel('time-interval/day')
plt.tick_params(axis='x',
                which='both',
                labelsize=10,
                labelcolor='#4d4f53',
                )
plt.ylabel('distance/km')
plt.tick_params(axis='y',
                which='both',
                labelsize=10,
                labelcolor='#4d4f53',
                )

plt.show()

''''
inpath=r"2.csv"# 文件路径
f=open(inpath,'r')
reader=csv.reader(f)

ans={}
for row in reader:
    if row[0] in ans:
        ans[row[0]]=max(row[1],ans[row[0]])
    else:
        ans[row[0]]=row[1]
f.close()
ans['2019/01']='0.0' # 2019/01月数据假设为0


year = ['2019', '2020']
month = ['02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
for y in year :
    for m in month  :
        if y+'/'+m  in ans.keys():
            continue
        if y=='2020' and m=='02':
            ans[y+'/'+m]= ans['2019/12']
        elif m not in ans.keys():
            ans[y+'/'+m]=ans[retype(y+'/'+str(int(m)-1))]
ans['2020/01']=ans['2019/12']


list_ans=[]
for item in ans.items():
    list_ans.append(item)


list_ans=sorted(list_ans,key=lambda i:tuple((i[0].split('/'))))
date,dis=[],[]
for key,value in list_ans:
    date.append(key)
    dis.append(value)
date=date[:len(date)-1]
dis=dis[:len(dis)-1]
print(dis)

'''
