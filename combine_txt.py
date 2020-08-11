# *************
# 合并txt文件
# ************

import os
str='front_right'
for i in range(0,7):
    with open('/media/autolab/disk_3T/caiyingfeng/6DOF/F1/'+i.__str__()+'_camera_'+str+'.txt',encoding='utf-8') as f:
        for line in f.readlines():
            with open('/media/autolab/disk_3T/caiyingfeng/6DOF/F1/'+str+'.txt',"a") as fp:
                fp.write(line)
