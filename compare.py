import os


dir_path = '/media/autolab/disk_3T/caiyingfeng/huawei/0711/F1/front_left/'

image_name_list=os.listdir(dir_path)

image_name_list.sort()
print(len(image_name_list))
f=open('/media/autolab/disk_3T/caiyingfeng/6DOF/0711/image_name/front_left.txt')#时间戳位姿
f_dof=list(f)
f_dof.sort()
print(len(f_dof))
count=0
for i in range(0,len(f_dof)):
    name=f_dof[i].split(' ',-1)[0]
    flag=0
    for j in range(0,len(image_name_list)):
        # print(image_name_list[j])
        if(('front_left/'+image_name_list[j])==name):
            flag=1
            break
    if flag==0:
        count+=1
        print(name)
    # break
print(count)
