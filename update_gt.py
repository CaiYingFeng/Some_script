import os
from pathlib import Path
from pyquaternion import Quaternion
from scipy.spatial.transform import Rotation as R
import numpy as np
gt=open('/media/autolab/disk_4T/cyf/localization/out/eval/aachen/0711_front_center20to1.txt')#time tx ty tz qx qy qz qw
gt_list=list(gt)
for str_dof in gt_list:
    qw = float(str_dof[7])        
    qx = float(str_dof[4])
    qy = float(str_dof[5])
    qz = float(str_dof[6])

    tx = float(str_dof[1])
    ty = float(str_dof[2])
    tz = float(str_dof[3])

    r = R.from_quat([qx,qy,qz,qw])
    rotation = r.as_matrix()
    translation = np.asarray([tx,ty,tz])
    R_T= np.eye(4)
    R_T[:3,:3]=rotation
    R_T[:3,3]=translation

    change=np.array([
        [1.000,-0.006,-0.025,19563.801],
        [0.006,1.000,-0.003,-1978.597],
        [0.025,0.003,1.000,-18458.740],
        [0.000,0.000,0.000,1.000]])     

    new=change.dot(R_T)
    rotation=new[:3,:3]
    translation=new[:3,3]



    r = R.from_matrix(rotation)
    r2=r.as_quat()
    xyz=translation