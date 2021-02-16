from PIL import Image
import cv2


def CNN(s):
    return 1

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
            res.append(CNN(image_name))

    return sum(res)/len(res)

a=proVedio(r"C:\Users\round\Desktop\2021MCM_ProblemC_Files\ATT3197_Back_Yard_2020-10-06T11_49_33-0700.mp4")
print(a)