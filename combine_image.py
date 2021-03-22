import os
from PIL import Image
from tqdm import tqdm
from multiprocessing import Pool
from multiprocessing import Process
import multiprocessing
import math


def join(png1, png2, png3, result):
    img1, img2, img3 = Image.open(png1), Image.open(png2), Image.open(png3)
    size1, size2, size3= img1.size, img2.size, img3.size  # 获取两张图片的大小
    # joint = Image.new('RGB', (int(size1[0]/2+size2[0]+size3[0]/2), int(size1[1])))
    joint = Image.new('RGB', (1920*2,1200))
    # 新建一张新的图片
    # 因为拼接的图片的高都是一样，所以高为固定值
    # 宽为中间图加两侧的一半
    loc1, loc2 ,loc3 = (0, 0), (960, 0), (1920,0)
    # 两张图片的位置
    # a-------------
    # |            |
    # |            |
    # |            |
    # |            |
    # |            |
    # b------------|
    # |            |
    # |            |
    # |            |
    # |            |
    # |------------|

    # 位置都是以该图片的左上角的坐标决定
    # 第一张图片的左上角为a点，a的坐标为(0,0)
    # 第二张图片的左上角为b点，a的横坐标为0，纵坐标为第一张图片的纵坐标减去第二张图片上移的size: (0, size[1]-size)

    joint.paste(img1, loc1)
    joint.paste(img3, loc3)
    joint.paste(img2, loc2)
    # 因为需要让第一张图片放置在图层的最上面,所以让第一张图片最后最后附着上图片上
    joint.save(result)




    
# dir_path = '/media/autolab/disk_3T/caiyingfeng/huawei/0711/F1/front_left_20to1'
dir_path = '/media/autolab/disk_3T/caiyingfeng/huawei/0808/B1/front_left'
image_name_list=os.listdir(dir_path)
image_name_list.sort()
image_path_list1=[os.path.join(dir_path,image_name)for image_name in image_name_list]

# dir_path = '/media/autolab/disk_3T/caiyingfeng/huawei/0711/F1/front_center_20to1'
dir_path = '/media/autolab/disk_3T/caiyingfeng/huawei/0808/B1/front_center_5to1'
image_name_list=os.listdir(dir_path)
image_name_list.sort()
image_path_list2=[os.path.join(dir_path,image_name)for image_name in image_name_list]

# dir_path = '/media/autolab/disk_3T/caiyingfeng/huawei/0711/F1/front_right_20to1'
dir_path = '/media/autolab/disk_3T/caiyingfeng/huawei/0808/B1/front_right'
image_name_list=os.listdir(dir_path)
image_name_list.sort()
image_path_list3=[os.path.join(dir_path,image_name)for image_name in image_name_list]

def combine_image(s_index,e_index):
    for i in tqdm(range(s_index,e_index)):
        png1=image_path_list1[5*i]#front_left
        png2=image_path_list2[i]#front_center
        png3=image_path_list3[5*i]#front_right
        # result='/media/autolab/disk_3T/caiyingfeng/huawei/0711/F1/fc_20to1/'+image_path_list2[i].split('/')[-1]
        result='/media/autolab/disk_3T/caiyingfeng/huawei/0808/B1/fc_5to1/'+image_path_list2[i].split('/')[-1]
        join(png1, png2, png3, result)
        

num_thread=12
index=math.floor(len(image_path_list2)/num_thread)
pool = multiprocessing.Pool(processes=num_thread)

for i in range(num_thread):
    if i<num_thread-1:
        pool.apply_async(combine_image,(index*i, index*(i+1)))
    elif i==num_thread-1:
        pool.apply_async(combine_image,(index*i, len(image_path_list2)))

pool.close()
pool.join()