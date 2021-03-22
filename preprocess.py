#-*- coding: utf-8 -*-
##处理图片过亮的部分
import cv2
import numpy as np
from tqdm import tqdm
from PIL import Image,ImageStat
import math
import os
from multiprocessing import Pool
from multiprocessing import Process
import multiprocessing
def brightness( im_file ):
    im = Image.open(im_file)
    stat = ImageStat.Stat(im)
    gs = (math.sqrt(0.241*(r**2) + 0.691*(g**2) + 0.068*(b**2)) 
        for r,g,b in im.getdata())
    return sum(gs)/stat.count[0]



def process(image_path_list, image_name_list, s_index, e_index):
    
    for i in tqdm(range(s_index,e_index)):
        fn=image_path_list[i]
        thr=brightness( fn )

        img = cv2.imread(fn)

        w = img.shape[1]
        h = img.shape[0]


        for xi in range(0,w):
            for xj in range(0,h):
                #将像素值整体减少，设为原像素值的20%
                
                r=int(img[xj,xi,0])
                g=int(img[xj,xi,1])
                b=int(img[xj,xi,2])
                if math.sqrt(0.241*(r**2) + 0.691*(g**2) + 0.068*(b**2))>1.65*thr:
                    img[xj,xi,0]=int(img[xj,xi,0]*0.6)
                    img[xj,xi,1]=int(img[xj,xi,1]*0.6)
                    img[xj,xi,2]=int(img[xj,xi,2]*0.6)

                elif math.sqrt(0.241*(r**2) + 0.691*(g**2) + 0.068*(b**2))>1.6*thr:
                    img[xj,xi,0]=int(img[xj,xi,0]*0.8)
                    img[xj,xi,1]=int(img[xj,xi,1]*0.8)
                    img[xj,xi,2]=int(img[xj,xi,2]*0.8)

                elif math.sqrt(0.241*(r**2) + 0.691*(g**2) + 0.068*(b**2))>1.5*thr:
                    img[xj,xi,0]=int(img[xj,xi,0]*0.9)
                    img[xj,xi,1]=int(img[xj,xi,1]*0.9)
                    img[xj,xi,2]=int(img[xj,xi,2]*0.9)



        cv2.imwrite('/media/autolab/disk_3T/caiyingfeng/huawei/dark/'+image_name_list[i], img)

dir_path= "/media/autolab/disk_3T/caiyingfeng/huawei/mobile_query"
image_name_list=os.listdir(dir_path)
image_name_list.sort()
image_path_list=[os.path.join(dir_path,image_name)for image_name in image_name_list]

num_thread=16
index=math.floor(len(image_path_list)/num_thread)
pool = multiprocessing.Pool(processes=num_thread)

for i in range(num_thread):
    if i<num_thread-1:
        pool.apply_async(process,(image_path_list, image_name_list, index*i, index*(i+1)))
    elif i==num_thread-1:
        pool.apply_async(process,(image_path_list, image_name_list, index*i, len(image_path_list)))

pool.close()
pool.join()
