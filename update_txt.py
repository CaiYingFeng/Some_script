#用于更新时间戳位姿中图片名
import os


str=['left','center','right'] 
for i in range(0,3):
    dir_path = '/media/autolab/disk_3T/caiyingfeng/huawei/0808/B1/front_'+str[i]+'/'

    image_name_list=os.listdir(dir_path)
    image_name_list.sort() 

    f=open('/media/autolab/disk_3T/caiyingfeng/6DOF/0808/B1/front_'+str[i]+'.txt')#时间戳位姿
    f_dof=list(f)
    f.close

    filename='/media/autolab/disk_3T/caiyingfeng/6DOF/0808/B1/front_'+str[i]+'.txt'#要保存的目录
    with open(filename,'w') as f:
        for j in range(0,len(f_dof)):
            f.write(image_name_list[j][:14]+f_dof[j][21:])