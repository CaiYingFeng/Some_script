import os
from pathlib import Path
from pyquaternion import Quaternion
from scipy.spatial.transform import Rotation as R
import numpy as np
from tqdm import tqdm

def create_emptySfM_threecam(posefiles, emptySfM_path):
    print("Running create_emptySfM")

    #posefile:时间戳位姿文件，每行为 time tx ty tz qx qy qz qw ；time必须与图片同名（除后缀名）,eg:$pro/pose.txt
    #emptySfM:要存放的空SfM模型，一个文件夹，eg:$pro/emptySfM

    if not os.path.exists(emptySfM_path):
            os.makedirs(emptySfM_path)
    #创建images.txt
    i_path=Path(emptySfM_path , f'images.txt')#要保存的model的images.txt
    if os.path.exists(i_path):
        os.remove(i_path)
    image_id=1
    for posefile in posefiles:  
        f=open(posefile)#时间戳位姿,posefile
        pose=list(f)
        f.close

        for i in tqdm(range(0,len(pose))):
        # for i in tqdm(range(0,5353)):                
            with open(i_path, 'a') as f:
                str_dof=pose[i].split(' ')    
                name=str_dof[0]+'.jpg'#可能需要改成jpg等其他格式，视具体情况而定    要改
                qw = float(str_dof[7])        
                qx = float(str_dof[4])
                qy = float(str_dof[5])
                qz = float(str_dof[6])

                # tx = float(str_dof[1])-368516
                # ty = float(str_dof[2])-3459036
                # tz = float(str_dof[3])-15
                # tz=0
                # tx = float(str_dof[3])
                # ty = float(str_dof[1])
                # tz = float(str_dof[2])
                tx = float(str_dof[1])
                ty = float(str_dof[2])
                tz = float(str_dof[3])

                r = R.from_quat([qx,qy,qz,qw])
                rotation = r.as_matrix()
        
                translation = np.asarray([tx,ty,tz])
                xyz = -np.dot(np.linalg.inv(rotation),translation)
                xyz = np.reshape(xyz,(1,3))
        
                r = R.from_matrix(np.linalg.inv(rotation))
                r2=r.as_quat()
        

                k=image_id
                line=k.__str__()+' '
                line+=r2[3].__str__()+' '                                 
                line+=r2[0].__str__()+' '
                line+=r2[1].__str__()+' '
                line+=r2[2].__str__()+' '
        
                line+=xyz[0][0].__str__()+' '   
                line+=xyz[0][1].__str__()+' '
                line+=xyz[0][2].__str__()+' '
                line+="1"+' '
        
            
                
                line+=name.__str__()
                    
                f.write(line+'\n'+'\n')
                image_id+=1
            
                

    #创建cameras.txt

    cameras_path=Path(emptySfM_path , f'cameras.txt')
    if os.path.exists(cameras_path):
        os.remove(cameras_path)
    
    camera_type='PINHOLE'

    with open(cameras_path, 'a') as f:
        #left_front
        line='1'+' '
        line+=camera_type+' '
        line+='1920'+' '
        line+='1200'+' '
        line+='1073.592178'+' '+'1072.747494'+' '#fx fy
        line+='950.691541'+' '+'585.321928'#x0 y0
        f.write(line+'\n')
        #middle_front
        line='2'+' '
        line+=camera_type+' '
        line+='1920'+' '
        line+='1200'+' '
        line+='1077.319838'+' '+'1076.431366'+' '#fx fy
        line+='959.747465'+' '+'600.50007'#x0 y0
        f.write(line+'\n')
        #right_front
        line='3'+' '
        line+=camera_type+' '
        line+='1920'+' '
        line+='1200'+' '
        line+='1068.790865'+' '+'1068.63618'+' '#fx fy
        line+='971.96159'+' '+'577.820583'#x0 y0
        f.write(line+'\n')
        #right_left 0711
        line='4'+' '
        line+=camera_type+' '
        line+='1920'+' '
        line+='1200'+' '
        line+='1072.613144'+' '+'1072.495216'+' '#fx fy
        line+='933.757082'+' '+'579.491254'#x0 y0
        f.write(line)






    #创建points3D.txt
    points3d_path  =  Path(emptySfM_path , f'points3D.txt')
    if os.path.exists(points3d_path):
        os.remove(points3d_path)
    open(points3d_path,'w')
    print("Finished create_emptySfM")

# base_path='/media/autolab/disk_3T/caiyingfeng/huawei/0808/B1/gt/fusion_v6/'
base_path='/media/autolab/disk_3T/caiyingfeng/huawei/0808/B1/gt/fusion_v10/'
# posefiles=[base_path+'front_center_p0.txt',base_path+'front_center_r0.txt',base_path+'front_center_y0.txt',base_path+'front_center_original.txt']
posefiles=[base_path+'Lidar_0808_rpz0.txt']
emptySfM_path='/media/autolab/disk_4T/cyf/localization/Herarchical-Localization/outputs/lidar/xyz_sfm_empty_v10'

create_emptySfM_threecam(posefiles,emptySfM_path)