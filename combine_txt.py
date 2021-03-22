# *************
# 合并txt文件
# ************

import os
str='front_right'
for i in range(0,29):
    with open('/media/autolab/disk_3T/caiyingfeng/huawei/0808/B1/name_pose/'+i.__str__()+'_'+str+'.txt') as f:
        for line in f.readlines():
            with open('/media/autolab/disk_3T/caiyingfeng/huawei/0808/B1/name_pose/'+str+'.txt',"a") as fp:
                fp.write(line)

# str=['left','center','right']

# if os.path.exists('/media/autolab/disk_3T/caiyingfeng/6DOF/0808/B1/test.txt'):
#     os.remove('/media/autolab/disk_3T/caiyingfeng/6DOF/0808/B1/test.txt')

# for i in range(0,3):
#     with open('/media/autolab/disk_3T/caiyingfeng/6DOF/0808/B1/front_'+str[i]+'_5to1.txt',encoding='utf-8') as f:
#         for line in f.readlines():
#             with open('/media/autolab/disk_3T/caiyingfeng/6DOF/0808/B1/test.txt',"a") as fp:
#                 fp.write(line)


# if os.path.exists('/media/autolab/disk_3T/caiyingfeng/6DOF/0808/B1/front_5to1.txt'):
#     os.remove('/media/autolab/disk_3T/caiyingfeng/6DOF/0808/B1/front_5to1.txt')

# f=open('/media/autolab/disk_3T/caiyingfeng/6DOF/0808/B1/test.txt')
# dof=list(f)
# dof.sort()
# for i in range(0,len(dof)):
#     with open('/media/autolab/disk_3T/caiyingfeng/6DOF/0808/B1/front_5to1.txt',"a") as fp:
#         fp.write(dof[i])



# str=['left','center','right']

# if os.path.exists('/media/autolab/disk_3T/caiyingfeng/6DOF/0711/image_name/hw_val.txt'):
#     os.remove('/media/autolab/disk_3T/caiyingfeng/6DOF/0711/image_name/hw_val.txt')

# for i in range(0,3):
#     with open('/media/autolab/disk_3T/caiyingfeng/6DOF/0711/image_name/front_'+str[i]+'2.txt',encoding='utf-8') as f:
#         for line in f.readlines():
#             with open('/media/autolab/disk_3T/caiyingfeng/6DOF/0711/image_name/hw_val.txt',"a") as fp:
#                 fp.write(line)

# filelist=['cam03.txt','cam05.txt','cam06.txt','cam07.txt','cam08.txt']
# s='database'
# if os.path.exists('/media/autolab/disk_4T/cyf/hw/camera_pose/query/query_pose_3to1.txt'):
#     os.remove('/media/autolab/disk_4T/cyf/hw/camera_pose/query/query_pose_3to1.txt')

# for file in filelist:
#     with open('/media/autolab/disk_4T/cyf/hw/camera_pose/'+s+'/'+file,encoding='utf-8') as f:
#         for line in f.readlines():            

#             with open('/media/autolab/disk_4T/cyf/hw/camera_pose/'+s+'/'+s+'_pose.txt',"a") as fp:
                        
#                 fp.write(line)

# f=open('/media/autolab/disk_4T/cyf/hw/camera_pose/'+s+'/'+s+'_pose.txt')
# dof=list(f)
# dof.sort()
# for i in range(0,len(dof)):
#     with open('/media/autolab/disk_4T/cyf/hw/camera_pose/'+s+'/'+s+'_pose_sorted.txt',"a") as fp:
#         fp.write(dof[i])
