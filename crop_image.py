#裁剪图片
from PIL import Image
from tqdm import tqdm
import os
import math
import os
from multiprocessing import Pool
from multiprocessing import Process
import multiprocessing

def crop(image_path_list, out_path, s_index, e_index):
    for i in tqdm(range(s_index,e_index)):
        im_path=image_path_list[i]
        img = Image.open(im_path)
        width,height=img.size
        left=0
        upper=0
        right=width
        lower=height/3.0*2
        cropped = img.crop((left, upper, right, lower))  # (left, upper, right, lower)
        cropped.save(out_path+'/'+im_path.split('/')[-1])

dir_path= "/media/autolab/disk_3T/caiyingfeng/huawei/0808/B1/front_center_5to1"
image_name_list=os.listdir(dir_path)
image_name_list.sort()
image_path_list=[os.path.join(dir_path,image_name)for image_name in image_name_list]

out_path="/media/autolab/disk_3T/caiyingfeng/huawei/0808/B1/front_center_5to1_up"
# for i in tqdm(range(len(image_path_list))):
#     crop(image_path_list[i], out_path)

num_thread=16
index=math.floor(len(image_path_list)/num_thread)
pool = multiprocessing.Pool(processes=num_thread)

for i in range(num_thread):
    if i<num_thread-1:
        pool.apply_async(crop,(image_path_list, out_path, index*i, index*(i+1)))
    elif i==num_thread-1:
        pool.apply_async(crop,(image_path_list, out_path, index*i, len(image_path_list)))

pool.close()
pool.join()