import os

#改图片名称
# dir_path = '/media/autolab/disk_3T/caiyingfeng/mask/0711/front_center'
strfile=['0_front_center']
for s in strfile:
    dir_path = '/media/autolab/disk_3T/caiyingfeng/huawei/0808/B1/'+s
    image_name_list=os.listdir(dir_path)
    image_path_list=[os.path.join(dir_path,image_name)for image_name in image_name_list]
    image_path_list.sort()

    for image_name in image_path_list:
        # print(image_name)
        # print(image_name[:(len(image_name)-5)]+image_name[(len(image_name)-4):])
        # break
        print(image_name)
        
        # im_name=image_name[:(len(image_name)-29)]+image_name[(len(image_name)-23):]
        # print(im_name)
        # im_name=im_name[:(len(im_name)-13)]+'.'+im_name[(len(im_name)-13):]
        # print(im_name)
        im_name=image_name[:(len(image_name)-11)]+image_name[(len(image_name)-4):]
        # print(im_name)
        # print(im_name)

        os.rename(image_name,im_name)
    # break
    # os.rename(image_name,image_name[:(len(image_name)-15)]+image_name[(len(image_name)-8):])



#改txt文件中图片名称

# for i in range(0,1):

#     f=open('/media/autolab/disk_4T/cyf/hw/camera_pose/query/query_pose_sorted.txt')#时间戳位姿
#     f_dof=list(f)
#     f.close
#     filename='/media/autolab/disk_4T/cyf/hw/camera_pose/query/query_pose_changedname.txt'
#     with open(filename,'w') as f:
#         for j in range(0,len(f_dof)):
#             # print(f_dof[j][:19]+f_dof[j][21:])
#             f.write(f_dof[j][:19]+f_dof[j][21:])
#             # break


# dir_path = "/media/autolab/disk_3T/caiyingfeng/6DOF/0711/train_data/"
# image_list=os.listdir(dir_path)
# # image_list_path=[os.path.join(dir_path,image_list_name)for image_list_name in image_list]
# # print(image_list)
# for i in image_list:
#     print(i)
#     f=open(os.path.join("/media/autolab/disk_3T/caiyingfeng/6DOF/0711/train_data/",i))#时间戳位姿
#     f_dof=list(f)
#     f.close
#     # print("/media/autolab/disk_3T/caiyingfeng/6DOF/0711/train_data/changed/"+i)
#     filename=os.path.join("/media/autolab/disk_3T/caiyingfeng/6DOF/0711/changed/",i)
#     with open(filename,'w') as f:
#         for j in range(0,len(f_dof)):
#             f.write(f_dof[j][:(len(f_dof[j])-43)]+f_dof[j][(len(f_dof[j])-42):])