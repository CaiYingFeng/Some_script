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
# 将文件夹下的不同类别的文件夹中的部分图片转移到另一个文件夹下的相同类别的文件夹下，并删除原文件夹中的相应图片（类似于剪切）
# create_querylist()用于生成hfnet用的querylist
# ground_truth()生成查询图片位姿真值
# ************************
import cv2
import os
def transferPictures(dbpath,querypath):#dbpath：原始图片目录，用作建图数据；querypath：提出的
    if(os.path.exists(dbpath) and os.path.exists(querypath)):

        image_name_list=os.listdir(dbpath)
      
        image_name_list.sort()

        for i in range(0,len(image_name_list)):
            if i%50==0:#每隔50张取出一张作为查询图片
                img = cv2.imread(dbpath + "/" + image_name_list[i])
                cv2.imwrite(querypath + "/" + image_name_list[i], img)
                os.remove(dbpath + "/" + image_name_list[i])
    else:
        print("路径不存在")

                #print(image_name_list[i])

def create_querylist(queryimage_dir):

    image_name_list=os.listdir(queryimage_dir)
    image_name_list.sort()
    filename='/media/autolab/disk_3T/caiyingfeng/localization/data/aachen/query-list.txt'
    with open(filename,'w') as f:
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
        for i in range(0,len(f_dof),50):#与transferPictures提取频率一致
            str_dof=f_dof[i].split(' ',-1)
            str_name=im_name[i].split('/',-1)
            name=str_name[-1]
            name=name.strip("\n")

            with open(i_path, 'a') as f:   
                line=name.strip(".jpg")+' '  
                  
                line+=str_dof[1]+' '
                line+=str_dof[2]+' '
                line+=str_dof[3]+' '
                line+=str_dof[4]+' '
                line+=str_dof[5]+' '
                line+=str_dof[6]+' '
                line+=str_dof[7].strip("\n")+' '                 
                #print(line) 

                f.write(line+'\n')
    else:
        print("路径不存在")

# #这里传入所要读取文件夹的绝对路径，加引号（引号不能省略！）
                   
str="front_left"
#transferPictures("/media/autolab/disk_3T/caiyingfeng/huawei/0711/F1/"+str,"/media/autolab/disk_3T/caiyingfeng/localization/data/aachen/image/query_"+str)
#transferPictures("/media/autolab/disk_3T/caiyingfeng/mask/"+str,"/media/autolab/disk_3T/caiyingfeng/mask/query_"+str)
create_querylist('/media/autolab/disk_3T/caiyingfeng/localization/data/aachen/image/query_'+str+'/')
#ground_truth('/media/autolab/disk_3T/caiyingfeng/6DOF/F1/'+str+'.txt','/media/autolab/disk_3T/caiyingfeng/darknet/'+str+'.txt')#时间戳位姿,darknet用list













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

