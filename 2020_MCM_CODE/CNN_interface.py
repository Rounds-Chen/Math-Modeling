import pandas as pd
import cv2

# CNN训练
def CNN(s):
    return 5


#处理视频
process_every_n_frame=24 # 24帧取一张图片
def proVedio(filename):
    #ext=filename.split('.')[-1] # 文件拓展名
    cap=cv2.VideoCapture(filename)
    count_frame=0

    res=[]
    while(True):
        ret,frame=cap.read()
        if ret==False:
            break
        count_frame+=1

        if count_frame%process_every_n_frame==0 and ret==True:
            image_name=filename[:-4]+str(count_frame/process_every_n_frame)+'.jpg'
            cv2.imwrite(image_name,frame)
            res.append(CNN(image_name)) # 调用CNN训练

    return sum(res)/len(res)


def getProbs(data,dir):
    data['ImageProb']=data.apply(lambda row :CNN(dir+"\\"+str(row['FileName'])) if row['FileType'] in ['image/jpg','image/png'] else(proVedio(dir+"\\"+str(row['FileName'])) if row['FileType'] in ['video/quicktime','video/mp4'] else 0 ), axis=1 )
    return data

if __name__=='__main__':
    file=r'test.csv' # 包含ID-FileName的文件
    data=pd.read_csv(file)
    dir=r'' # dir-path
    data=getProbs(data,dir)
    data.to_csv('test.csv',encoding='utf-8-sig') # 数据写回原文件