import os

#改图片名称
dir_path = '/media/autolab/disk_3T/caiyingfeng/mask/0808/front_5to1/'
# dir_path = '/media/autolab/disk_3T/caiyingfeng/huawei/0808/B1/front_right/'
image_name_list=os.listdir(dir_path)
image_path_list=[os.path.join(dir_path,image_name)for image_name in image_name_list]
image_path_list.sort()

for image_name in image_path_list:

    # os.rename(image_name,image_name[:(len(image_name)-6)]+image_name[(len(image_name)-4):])
    os.rename(image_name,image_name[:(len(image_name)-10)]+image_name[(len(image_name)-8):])



#改txt文件中图片名称
# for i in range(0,29):

#     f=open('/media/autolab/disk_3T/caiyingfeng/6DOF/0808/B1/'+i.__str__()+'_camera_front_left.txt')#时间戳位姿
#     f_dof=list(f)
#     f.close
#     filename='/media/autolab/disk_3T/caiyingfeng/6DOF/0808/B1/'+i.__str__()+'_front_left.txt'
#     with open(filename,'w') as f:
#         for j in range(0,len(f_dof)):
#             f.write(f_dof[j][:14]+f_dof[j][21:])

