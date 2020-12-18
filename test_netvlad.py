import cv2
import os
import shutil

def transferPictures(image_name):#dbpath：原始图片目录；querypath：提出的
    image_path='/media/autolab/disk_3T/caiyingfeng/pytorch-NetVlad/data/'+image_name
    d_path='/media/autolab/disk_3T/caiyingfeng/localization/data/aachen/image/db/'+image_name.split('/',1)[0]
    if(os.path.exists(image_path) ):
        # if(not os.path.exists(d_path)):
        #     print(image_name+"目录不存在")
            # os.mkdir(d_path)
        shutil.copy(image_path,d_path+'-'+image_name.split('/',1)[1])

    else:
        print(image_name+"图片不存在")

f=open('/media/autolab/disk_3T/caiyingfeng/6DOF/0808/train_data/add/val_30k_db.txt')#时间戳位姿
f_dof=list(f)
print(len(f_dof))
for im in f_dof:
    im_name=im.split(' ',1)[0]
    transferPictures(im_name)
    # break