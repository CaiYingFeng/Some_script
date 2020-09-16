# *************
# 合并txt文件
# ************

import os
# str='front_right'
# for i in range(0,29):
#     with open('/media/autolab/disk_3T/caiyingfeng/6DOF/0808/B1/'+i.__str__()+'_camera_'+str+'.txt',encoding='utf-8') as f:
#         for line in f.readlines():
#             with open('/media/autolab/disk_3T/caiyingfeng/6DOF/0808/B1/'+str+'.txt',"a") as fp:
#                 fp.write(line)

str=['left','center','right']

if os.path.exists('/media/autolab/disk_3T/caiyingfeng/6DOF/0808/B1/test.txt'):
    os.remove('/media/autolab/disk_3T/caiyingfeng/6DOF/0808/B1/test.txt')

for i in range(0,3):
    with open('/media/autolab/disk_3T/caiyingfeng/6DOF/0808/B1/front_'+str[i]+'_5to1.txt',encoding='utf-8') as f:
        for line in f.readlines():
            with open('/media/autolab/disk_3T/caiyingfeng/6DOF/0808/B1/test.txt',"a") as fp:
                fp.write(line)


if os.path.exists('/media/autolab/disk_3T/caiyingfeng/6DOF/0808/B1/front_5to1.txt'):
    os.remove('/media/autolab/disk_3T/caiyingfeng/6DOF/0808/B1/front_5to1.txt')

f=open('/media/autolab/disk_3T/caiyingfeng/6DOF/0808/B1/test.txt')
dof=list(f)
dof.sort()
for i in range(0,len(dof)):
    with open('/media/autolab/disk_3T/caiyingfeng/6DOF/0808/B1/front_5to1.txt',"a") as fp:
        fp.write(dof[i])