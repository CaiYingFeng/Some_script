
#输入：time tx ty tz qx qy qz qw   :c2w
#输出：name qw,qx,qy,qz,tx,ty,tz   :w2c

import numpy as np
from pyquaternion import Quaternion
from scipy.spatial.transform import Rotation as R
import os
from pathlib import Path

cam='cam03_c2w'
if os.path.exists('/media/autolab/disk_4T/cyf/localization/out/eval/aachen/'+cam+'/estimate1.txt'):
        os.remove('/media/autolab/disk_4T/cyf/localization/out/eval/aachen/'+cam+'/estimate1.txt')
i_path='/media/autolab/disk_4T/cyf/localization/out/eval/aachen/'+cam+'/estimate1.txt'
f=open('/media/autolab/disk_4T/cyf/localization/out/eval/aachen/'+cam+'/'+cam+'.txt')
f_dof=list(f)
f.close
for i in range(0,len(f_dof)):
    str_dof=f_dof[i].split(' ',-1)             
    with open(i_path, 'a') as f:
        line=str_dof[0]+' '          
                
        line+=str_dof[7].strip("\n")+' '
        line+=str_dof[4]+' '
        line+=str_dof[5]+' '                            
        line+=str_dof[6]+' '

        line+=str_dof[1]+' '
        line+=str_dof[2]+' '
        line+=str_dof[3]+' '
                
        f.write(line+'\n')

f = open("/media/autolab/disk_4T/cyf/localization/out/eval/aachen/"+cam+"/estimate1.txt","r")#c2w:time qw,qx,qy,qz,tx,ty,tz,单纯换了个顺序


f_dof=list(f)
f_dof.sort()
f.close

i_path='/media/autolab/disk_4T/cyf/localization/out/eval/aachen/'+cam+'/'+cam+'_w2c.txt'#要保存w2c:name qw,qx,qy,qz,tx,ty,tz
for i in range(0,len(f_dof)):               
    str_dof=f_dof[i].split(' ',-1)
    with open(i_path, 'a') as f:
        qw = float(str_dof[1])        
        qx = float(str_dof[2])
        qy = float(str_dof[3])
        qz = float(str_dof[4])
        
        tx = float(str_dof[5])
        ty = float(str_dof[6])
        tz = float(str_dof[7])

        r = R.from_quat([qx,qy,qz,qw])
        rotation = r.as_matrix()
        
        translation = np.asarray([tx,ty,tz])
        xyz = -np.dot(np.linalg.inv(rotation),translation)
        xyz = np.reshape(xyz,(1,3))

        
        r = R.from_matrix(np.linalg.inv(rotation))
        r2=r.as_quat()#qx,qy,qz,qw

        line=str_dof[0]+".png "#time

        #qw qx qy qz
        line+=r2[3].__str__()+' '
        line+=r2[0].__str__()+' '
        line+=r2[1].__str__()+' '
        line+=r2[2].__str__()+' '

        #tx ty tz
        line+=(xyz[0][0]).__str__()+' '   
        line+=(xyz[0][1]).__str__()+' '
        line+=(xyz[0][2]).__str__()
        #print(line)

        f.write(line+'\n')