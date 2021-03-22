

# #**********************************#
# # 用于生成darknet用image_names.txt #
# #**********************************#

import os
# str_file=['db','cam03','cam05','cam06','cam07','cam08']
# for strfile in str_file:
# #dir_path='/media/autolab/disk_3T/caiyingfeng/huawei/0711/F1/0_back_left/'

# #dir_path = '/media/autolab/disk_3T/caiyingfeng/huawei/0711/F1/0_back_right/'
# #dir_path = '/media/autolab/disk_3T/caiyingfeng/huawei/0711/F1/1_front_center/' 
# # dir_path = '/media/autolab/disk_3T/caiyingfeng/huawei/0808/B1/'+str_file+'/' 
# # dir_path = '/media/autolab/disk_3T/caiyingfeng/huawei/0711/F1/front_center/'
# # dir_path='/media/autolab/disk_3T/caiyingfeng/localization/Hierarchical-Localization/datasets/huawei/IMAGE/images/query_0707'
# strfile='front_center_5to1'
# dir_path = '/media/autolab/disk_3T/caiyingfeng/huawei/0808/B1/'+strfile
# image_name_list=os.listdir(dir_path)
# image_name_list.sort()
# image_path_list=[os.path.join(dir_path,image_name)for image_name in image_name_list]
# # # image_path_list.sort()
# # filename='/media/autolab/disk_3T/caiyingfeng/darknet/imagelist/0808/'+str_file+'.txt'
# # filename='/media/autolab/disk_3T/caiyingfeng/darknet/imagelist/'+strfile+'.txt'
# filename='/media/autolab/disk_3T/caiyingfeng/huawei/0808/B1/'+strfile+'.txt'
# with open(filename,'w') as f:
#     for i in range(0,len(image_name_list)):
#         f.write(image_name_list[i]+'\n')


# #**********************************#
# # 用于生成colmap定位用imagelist.txt #
# #**********************************#

# import os


# dir_path = '/media/autolab/disk_3T/caiyingfeng/huawei/0711/F1/front_right/'

# image_name_list=os.listdir(dir_path)

# image_name_list.sort()
# filename='/media/autolab/disk_3T/caiyingfeng/huawei/0711/B1/front_right_list2.txt'

# with open(filename,'w') as f:
#     for i in range(2,len(image_name_list),3):
#         f.write('front_right/'+image_name_list[i]+'\n')


#**********************************************#
# 用于生成hfent-localization用query.txt
# 
# def ground_truth(time_path,name_path):用于生成查询图片的位姿真值groundtruth.txt #
#**********************************************#
# ************************第一步**********************
<<<<<<< HEAD
import os
dir_path = "/media/autolab/disk_4T/cyf/localization/data/aachen/image/query"
image_name_list=os.listdir(dir_path)
image_name_list.sort()
filename="/media/autolab/disk_4T/cyf/localization/data/aachen/cam03.txt"
with open(filename,'w') as f:
    for i in range(0,len(image_name_list)):
        f.write('query/'+image_name_list[i]+' PINHOLE 1920 1020 1938.34 1937.10 959.5 509.5\n')
=======
# import os
# dir_path = "/media/autolab/disk_4T/cyf/localization/data/aachen/image/query"
# image_name_list=os.listdir(dir_path)
# image_name_list.sort()
# filename="/media/autolab/disk_4T/cyf/localization/data/aachen/cam03.txt"
# with open(filename,'w') as f:
#     for i in range(0,len(image_name_list)):
#         f.write('query/'+image_name_list[i]+' PINHOLE 1920 1020 1938.34 1937.10 959.5 509.5\n')
>>>>>>> 781ea4ee083b4ef2a11abdf8509bd86ad16c661b



# # *************************第二步*******************************
# import os
# def ground_truth(time_path,name_path):
#     f=open(time_path)#所有图片的位姿
#     f_dof=list(f)
#     f.close
#     f=open(name_path)#所有图片的name
#     im_name=list(f)
#     im_name.sort()
#     f.close()

#     dir_path = '/media/autolab/disk_3T/caiyingfeng/localization/data/aachen/image/query/' 
#     query_name_list=os.listdir(dir_path)
#     query_name_list.sort()#查询图片的name

#     i_path='/media/autolab/disk_3T/caiyingfeng/stamped_groundtruth.txt'
#     for i in range(0,len(query_name_list)):
#         for j in range(0,len(im_name)):
#             str_name=im_name[j].split('/',-1)
#             name=str_name[-1]
#             name=name.strip("\n")
#             if query_name_list[i]==name:           
#                 str_dof=f_dof[i].split(' ',-1)

#                 with open(i_path, 'a') as f:   
#                     line=name.strip(".jpg")+' '    
#                     line+=str_dof[1]+' '
#                     line+=str_dof[2]+' '
#                     line+=str_dof[3]+' '
#                     line+=str_dof[4]+' '
#                     line+=str_dof[5]+' '
#                     line+=str_dof[6]+' '
#                     line+=str_dof[7].strip("\n")+' ' 
        
        
#                     f.write(line+'\n')





# ground_truth('/media/autolab/disk_3T/caiyingfeng/6DOF/F1/front.txt','/media/autolab/disk_3T/caiyingfeng/darknet/front.txt')#时间戳位姿,darknet用list