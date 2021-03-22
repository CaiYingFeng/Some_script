#评估轨迹使用，（若是image.bin中提取，则先去huawei.ipynb处理），再经过此处处理即可得到c2w可输入rpg_trajectory_evaluation中评估
#用于转换相机到世界和世界到相机
import numpy as np
from pyquaternion import Quaternion
from scipy.spatial.transform import Rotation as R
import os
from pathlib import Path

#从hfnet的pose里面提取位姿
#输入：name qw,qx,qy,qz,tx,ty,tz   :w2c
#输出：time tx ty tz qx qy qz qw   :c2w
cam='cam03_0107'
if os.path.exists('/media/autolab/disk_4T/cyf/evo/'+cam+'/estimate1.txt'):
        os.remove('/media/autolab/disk_4T/cyf/evo/'+cam+'/estimate1.txt')
i_path='/media/autolab/disk_4T/cyf/evo/'+cam+'/estimate1.txt'
f=open('/media/autolab/disk_4T/cyf/evo/'+cam+'/'+cam+'_poses.txt')
i_path='/media/autolab/disk_4T/cyf/evo/'+cam+'/estimate1.txt'
f=open('/media/autolab/disk_4T/cyf/evo/'+cam+'/'+cam+'_poses.txt')
f_dof=list(f)
f.close
for i in range(0,len(f_dof)):
    str_dof=f_dof[i].split(' ',-1)             
    with open(i_path, 'a') as f:
        line=str_dof[0].strip(".png")+' '          
                
        line+=str_dof[5]+' '
        line+=str_dof[6]+' '
        line+=str_dof[7].strip("\n")+' ' 
                
                
        line+=str_dof[2]+' '
        line+=str_dof[3]+' '
        line+=str_dof[4]+' '
        line+=str_dof[1]+' '
                
                
        
        f.write(line+'\n')




#f = open("/media/autolab/disk_3T/caiyingfeng/stamped_groundtruth.txt","r")#w2c:time tx ty tz qx qy qz qw 
f = open("/media/autolab/disk_4T/cyf/evo/"+cam+"/estimate1.txt","r")#w2c:time tx ty tz qx qy qz qw 


f_dof=list(f)
f_dof.sort()#因为groundtruth是三个相机按序来的，所以不估计值也不sort
f.close
#i_path=Path('/media/autolab/disk_3T/caiyingfeng/rpg_trajectory_evaluation/eva',f'stamped_groundtruth.txt')#要保存的c2w:time tx ty tz qx qy qz qw 
i_path=Path('/media/autolab/disk_4T/cyf/evo/'+cam,f'estimate.txt')#要保存的c2w:time tx ty tz qx qy qz qw 
for i in range(0,len(f_dof)):               
    str_dof=f_dof[i].split(' ',-1)
    with open(i_path, 'a') as f:
        qw = float(str_dof[7])        
        qx = float(str_dof[4])
        qy = float(str_dof[5])
        qz = float(str_dof[6])
        
        tx = float(str_dof[1])
        ty = float(str_dof[2])
        tz = float(str_dof[3])
        #print(qw)
#         r = Quaternion(qw, qx, qy, qz)
#         rotation = r.rotation_matrix
        r = R.from_quat([qx,qy,qz,qw])
        rotation = r.as_matrix()
        
        translation = np.asarray([tx,ty,tz])
        xyz = -np.dot(np.linalg.inv(rotation),translation)
        xyz = np.reshape(xyz,(1,3))
#         print(xyz)
#         print(xyz[0][1])
        
        r = R.from_matrix(np.linalg.inv(rotation))
        r2=r.as_quat()
        
        #print(res)

        line=str_dof[0]+" "#time

        #tx ty tz
        # line+=(xyz[0][0]+368516).__str__()+' '   
        # line+=(xyz[0][1]+3459036).__str__()+' '
        # line+=(xyz[0][2]+15).__str__()+' '
        line+=(xyz[0][0]).__str__()+' '   
        line+=(xyz[0][1]).__str__()+' '
        line+=(xyz[0][2]).__str__()+' '


        #qx qy qz qw
        line+=r2[0].__str__()+' '
        line+=r2[1].__str__()+' '
        line+=r2[2].__str__()+' '
        line+=r2[3].__str__()
        #print(line)


        #break
 
        f.write(line+'\n')


