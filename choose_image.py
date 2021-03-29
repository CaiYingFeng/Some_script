from tqdm import tqdm
#用于从一个文件夹中提取部分图片


# # ******************************
# # 对图片进行采样，没什么屁用了
# # ******************************
# import cv2
# import os

# def read_directory(start_path,end_path):

#     image_name_list=os.listdir(start_path)
      
#     image_name_list.sort()

#     for i in range(0,len(image_name_list)):
#         if i%50==0:
#             continue

#             #print(image_name_list[i])
#         img = cv2.imread(start_path + "/" + image_name_list[i])
#         cv2.imwrite(end_path + "/" + image_name_list[i], img)


# #这里传入所要读取文件夹的绝对路径，加引号（引号不能省略！）
# read_directory("/media/autolab/disk_3T/caiyingfeng/huawei/0711/F1/front_center","/media/autolab/disk_3T/caiyingfeng/localization/data/aachen/image/fc")
# read_directory("/media/autolab/disk_3T/caiyingfeng/mask/front_center","/media/autolab/disk_3T/caiyingfeng/mask/fc")



# ************************
# transferPictures()用于分割建图用图片和查询图片
# 将文件夹下的不同类别的文件夹中的部分图片转移到另一个文件夹下的相同类别的文件夹下，（可选：并删除原文件夹中的相应图片（类似于剪切））
# create_querylist()用于生成hfnet用的querylist
# ground_truth()生成查询图片位姿真值,rpg直接可以用了
# ************************
import cv2
import os
import shutil

def transferPictures(step, dbpath, querypath):#dbpath：原始图片目录，用作建图数据；querypath：提出的
    if(os.path.exists(dbpath) and os.path.exists(querypath)):

        image_name_list=os.listdir(dbpath)
      
        image_name_list.sort()

        for i in tqdm(range(0,len(image_name_list),step)):
            # if i%50==0:#每隔50张取出一张作为查询图片
                # img = cv2.imread(dbpath + "/" + image_name_list[i])
                # cv2.imwrite(querypath + "/" + image_name_list[i], img)
                # os.remove(dbpath + "/" + image_name_list[i])
                shutil.copy(dbpath + "/" + image_name_list[i],querypath + "/" + image_name_list[i])


    else:
        print("路径不存在")

                #print(image_name_list[i])
def pick_timestamp(step,fromstamp,endstamp):
    f=open(fromstamp)#time tx ty tz qx qy qz qw正好是rpg所需
    f_dof=list(f)
    f.close
    for i in range(0,len(f_dof),step):#根据每隔几张取图建图定步长
        with open(endstamp, 'a') as f:
            f.write(f_dof[i])


    



def create_querylist(queryimage_dir):

    image_name_list=os.listdir(queryimage_dir)
    image_name_list.sort()
    filename='/media/autolab/disk_3T/caiyingfeng/localization/data/aachen/query_front_center_0711.txt'
    with open(filename,'a') as f:
        for i in range(0,len(image_name_list)):
            f.write('query/'+image_name_list[i]+' PINHOLE 1920 1200 2304.0 2304.0 960.0 600.0\n')

def ground_truth(time_path,name_path):
    if(os.path.exists(time_path) and os.path.exists(name_path)):
        f=open(time_path)#time tx ty tz qx qy qz qw正好是rpg所需
        f_dof=list(f)
        f.close
        f=open(name_path)#darknet用过的imagename.txt
        im_name=list(f)
        im_name.sort()
        f.close()
        i_path='/media/autolab/disk_3T/caiyingfeng/stamped_groundtruth.txt'
        for i in range(0,len(f_dof),20):#与transferPictures提取频率一致
            str_dof=f_dof[i].split(' ',-1)
            str_name=im_name[i].split('/',-1)
            name=str_name[-1]
            name=name.strip("\n")

            with open(i_path, 'a') as f:   
                line=name.strip(".jpg")+' '  
                  
                # line+=(float(str_dof[1])-368500).__str__()+' '
                # line+=(float(str_dof[2])-3459000).__str__()+' '
                # line+=(float(str_dof[3])-15).__str__()+' '

                line+=str_dof[1]+' '
                line+=str_dof[2]+' '
                line+=str_dof[3]+' '
                line+=str_dof[4]+' '
                line+=str_dof[5]+' '
                line+=str_dof[6]+' '
                line+=str_dof[7].strip("\n")               
                #print(line) 

                f.write(line+'\n')
    else:
        print("路径不存在")

# #这里传入所要读取文件夹的绝对路径，加引号（引号不能省略！）
                   
s="front_right"
# transferPictures("/media/autolab/disk_3T/caiyingfeng/huawei/0711/F1/"+str,"/media/autolab/disk_3T/caiyingfeng/localization/data/aachen/image/query")
# transferPictures("/media/autolab/disk_3T/caiyingfeng/mask/0711/"+str,"/media/autolab/disk_3T/caiyingfeng/mask/0711/query_"+str)
# create_querylist('/media/autolab/disk_3T/caiyingfeng/localization/data/aachen/image/query/')
# ground_truth('/media/autolab/disk_3T/caiyingfeng/6DOF/0711/F1/1_camera_front_center.txt','/media/autolab/disk_3T/caiyingfeng/darknet/imagelist/0711/'+str+'.txt')#时间戳位姿,darknet用list

# transferPictures(10,"/media/autolab/disk_3T/caiyingfeng/huawei/0711/F1/"+s,"/media/autolab/disk_3T/caiyingfeng/huawei/0711/F1/front_10to1")
# print("left 完成")
# transferPictures(1,"/media/autolab/disk_3T/caiyingfeng/huawei/0711/F1/front_3to1","/media/autolab/disk_3T/caiyingfeng/huawei/10to1")
# print("center 完成")
# transferPictures("/media/autolab/disk_3T/caiyingfeng/huawei/0808/B1/front_right","/media/autolab/disk_3T/caiyingfeng/localization/data/aachen/image/query")
# print("right 完成")
# strflie=['front_center_align','front_left_align','front_right_align']
strflie=['front_center','front_left','front_right']
for s in strflie:

#     # transferPictures(2,"/media/autolab/disk_4T/cyf/hw/database/"+s,"/media/autolab/disk_4T/cyf/hw/database/2to1")
# # create_querylist('/media/autolab/disk_3T/caiyingfeng/localization/data/aachen/image/query')
# # ground_truth('/media/autolab/disk_3T/caiyingfeng/6DOF/0808SC/B1/2_camera_front_center.txt','/media/autolab/disk_3T/caiyingfeng/darknet/imagelist/0808/'+str+'.txt')#时间戳位姿,darknet用list
# #
    # transferPictures(3,"/media/autolab/disk_3T/caiyingfeng/huawei/0711/F1/"+s,"/media/autolab/disk_3T/caiyingfeng/huawei/0711/F1/front_3to1")
    pick_timestamp(10,'/media/autolab/disk_3T/caiyingfeng/huawei/0808/B1/gt/fusion_v12/'+s+'.txt','/media/autolab/disk_3T/caiyingfeng/huawei/0808/B1/gt/fusion_v12/'+s+'_10to1.txt')









# f=open('/media/autolab/disk_3T/caiyingfeng/stamped_groundtruth.txt')
# f_dof=list(f)
# f_dof.sort()
# f.close
# # print(f_dof[0])
# # print(len(f_dof))

# f=open('/media/autolab/disk_3T/caiyingfeng/rpg_trajectory_evaluation/front_eva/stamped_traj_estimate.txt')
# im_name=list(f)
# f.close

# # print(im_name[0])
# # print(len(im_name))
# i_path='/media/autolab/disk_3T/caiyingfeng/stamped_groundtruth1.txt'
# for i in range(0,len(f_dof)):
#     str_name=im_name[i].split(" ",-1)
#     name=str_name[0]
#     str_dof=f_dof[i].split(' ',-1)
#     with open(i_path, 'a') as f:   
#         line=name+' ' 
        
         
#         line+=str_dof[1]+' '
#         line+=str_dof[2]+' '
#         line+=str_dof[3]+' '
#         line+=str_dof[4]+' '
#         line+=str_dof[5]+' '
#         line+=str_dof[6]+' '
#         line+=str_dof[7].strip("\n")+' ' 
#         #print(line) 
#         f.write(line+'\n')

