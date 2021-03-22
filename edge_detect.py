import cv2
from PIL import Image,ImageFilter
import random,sys
from tqdm import tqdm
import os
import math
import os
from multiprocessing import Pool
from multiprocessing import Process
import multiprocessing
def detect(image_path_list, out_path, s_index, e_index):
    for i in tqdm(range(s_index,e_index)):
        im_path = image_path_list[i]
        img = Image.open(im_path)
        img = img.convert("RGB") 
        imgfilted_c = img.filter(ImageFilter.CONTOUR)
        # imgfilted_c = imgfilted_c.filter(ImageFilter.SMOOTH_MORE)
        imgfilted_c.save(out_path+'/'+im_path.split('/')[-1])
        # img = cv2.imread(im_path)
        # img2gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        # c_canny_img = cv2.Canny(img2gray,50,150)
        # cv2.imwrite(out_path+'/'+im_path.split('/')[-1], c_canny_img)


dir_path= "/media/autolab/disk_3T/caiyingfeng/huawei/0808/B1/front_center_5to1_up"
# dir_path= "/media/autolab/disk_3T/caiyingfeng/huawei/mobile_query_down"
image_name_list=os.listdir(dir_path)
image_name_list.sort()
image_path_list=[os.path.join(dir_path,image_name)for image_name in image_name_list]

out_path="/media/autolab/disk_3T/caiyingfeng/huawei/0808/B1/front_center_5to1_edge"
# out_path= "/media/autolab/disk_3T/caiyingfeng/huawei/mobile_query_edge"
# detect(image_path_list, out_path, 1, 5)
num_thread=16
index=math.floor(len(image_path_list)/num_thread)
pool = multiprocessing.Pool(processes=num_thread)

for i in range(num_thread):
    if i<num_thread-1:
        pool.apply_async(detect,(image_path_list, out_path, index*i, index*(i+1)))
    elif i==num_thread-1:
        pool.apply_async(detect,(image_path_list, out_path, index*i, len(image_path_list)))

pool.close()
pool.join()