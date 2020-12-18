#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by victor

# 本模块的功能:<更改图片尺寸>

import os
import os.path
from PIL import Image
import cv2
import argparse
'''
filein: 输入图片
fileout: 输出图片
width: 输出图片宽度
height:输出图片高度
type:输出图片类型（png, gif, jpeg...）
'''
parser = argparse.ArgumentParser(description='v_name')
parser.add_argument('--name', type=str)

def ResizeImage(filein, fileout, width, height, type):
    # img = Image.open(filein)
    img = cv2.imread(filein)
    # img = cv2.cvtColor(img , cv2.COLOR_RGB2GRAY)
    out = cv2.resize(img,
    (width, height),interpolation=cv2.INTER_CUBIC)
    # out = img.resize((width, height),Image.ANTIALIAS)
    #resize image with high-quality
    cv2.imwrite(fileout,out)
if __name__ == "__main__":
    opt = parser.parse_args()
    # video_name=['VID_20200905_130904','VID_20200905_130924','VID_20200905_130951','VID_20200905_131022','VID_20200905_131100','VID_20200905_131118',
    #         'VID_20200905_133723','VID_20200905_133959','VID_20200905_134239','VID_20200905_134305','VID_20200905_135453','VID_20200905_135535','VID_20200905_135602','VID_20200905_135859','VID_20200905_153947','VID_20200905_154132','VID_20200905_154810']
    # video_name=['front_center_0808','front_center','front_left','front_right','front_left_0808','front_right_08008']
    video_name=opt.name
    print(opt.name)
    # for v_n in video_name:
    v_n=video_name
    # dir_path_in = '/media/autolab/disk_3T/caiyingfeng/pytorch-NetVlad/data/'+v_n
    dir_path_in='/media/autolab/disk_3T/caiyingfeng/huawei/0808/B1/front_5to1'
    dir_path_out='/media/autolab/disk_3T/caiyingfeng/pytorch-NetVlad/data/db'

    # dir_path_out = '/media/autolab/disk_3T/caiyingfeng/pytorch-NetVlad/data/changed/'+v_n
    if not os.path.exists(dir_path_out):
        os.makedirs(dir_path_out)
    # dir_path_out = '/media/autolab/disk_3T/caiyingfeng/20200905Mobile/Phone1'
    image_name_list=os.listdir(dir_path_in)

    image_path_list=[os.path.join(dir_path_in,image_name)for image_name in image_name_list]
    image_path_list.sort()
    

    for image_name in image_path_list:
        # print(image_name)
        im_name=image_name.split('/')[-1]
        # print(im_name)
        width = 960
        height = 600
        type = 'jpg'
    
        ResizeImage(image_name, dir_path_out+'/'+im_name, width, height, type)

