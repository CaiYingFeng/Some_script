import os
from pathlib import Path
from pyquaternion import Quaternion
from scipy.spatial.transform import Rotation as R
import numpy as np
from tqdm import tqdm
def create_emptySfM_multi( image_path, posefiles, emptySfM_path):
    print("Running create_emptySfM")

    #posefile:时间戳位姿文件，每行为 time tx ty tz qx qy qz qw ；time必须与图片同名（除后缀名）,eg:$pro/pose.txt
    #emptySfM:要存放的空SfM模型，一个文件夹，eg:$pro/emptySfM

    if not os.path.exists(emptySfM_path):
            os.makedirs(emptySfM_path)
    #创建images.txt
    image_name_list=os.listdir(image_path)
    image_name_list.sort()
    i_path=Path(emptySfM_path , f'images.txt')#要保存的model的images.txt
    if os.path.exists(i_path):
        os.remove(i_path)
    pose=[]
    pose_index=[]
    for posefile in posefiles:
        f=open(posefile)#时间戳位姿,posefile
        f_dof=list(f)
        pose_index.append(len(f_dof))
        pose+=f_dof
        f.close

    for i in tqdm(range(len(image_name_list))):
        for j in range(len(pose)):
            str_dof=pose[j].split(' ',-1)
            if image_name_list[i].strip('.jpg')==str_dof[0]:
                name=str_dof[0]+'.jpg'#可能需要改成jpg等其他格式，视具体情况而定                   
                with open(i_path, 'a') as f:

                    qw = float(str_dof[7])        
                    qx = float(str_dof[4])
                    qy = float(str_dof[5])
                    qz = float(str_dof[6])

                    tx = float(str_dof[1])-368516
                    ty = float(str_dof[2])-3459036
                    tz = float(str_dof[3])-15

                    r = R.from_quat([qx,qy,qz,qw])
                    rotation = r.as_matrix()
            
                    translation = np.asarray([tx,ty,tz])
                    xyz = -np.dot(np.linalg.inv(rotation),translation)
                    xyz = np.reshape(xyz,(1,3))
            
                    r = R.from_matrix(np.linalg.inv(rotation))
                    r2=r.as_quat()
            

                    k=i+1
                    line=k.__str__()+' '
                    line+=r2[3].__str__()+' '                                 
                    line+=r2[0].__str__()+' '
                    line+=r2[1].__str__()+' '
                    line+=r2[2].__str__()+' '
            
                    line+=xyz[0][0].__str__()+' '   
                    line+=xyz[0][1].__str__()+' '
                    line+=xyz[0][2].__str__()+' '

                    if j<pose_index[0]:
                        line+="1"+' '
                    elif j>=pose_index[0] and j<pose_index[0]+pose_index[1]:
                        line+="2"+' '
                    elif j>=pose_index[0]+pose_index[1] and j<pose_index[0]+pose_index[1]+pose_index[2]:
                        line+="3"+' '
                    elif j>pose_index[0]+pose_index[1]+pose_index[2]:
                        print('something error')
                    line+=name.__str__()
                        
                    f.write(line+'\n'+'\n')
                    break
                        

    #创建cameras.txt

    cameras_path=Path(emptySfM_path , f'cameras.txt')
    if os.path.exists(cameras_path):
        os.remove(cameras_path)
    
    camera_type='PINHOLE'

    with open(cameras_path, 'a') as f:
        
        #left_front 0808
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

def create_emptySfM(posefile, emptySfM_path):
    print("Running create_emptySfM")

    #posefile:时间戳位姿文件，每行为 time tx ty tz qx qy qz qw ；time必须与图片同名（除后缀名）,eg:$pro/pose.txt
    #emptySfM:要存放的空SfM模型，一个文件夹，eg:$pro/emptySfM

    if not os.path.exists(emptySfM_path):
            os.makedirs(emptySfM_path)
    #创建images.txt
    i_path=Path(emptySfM_path , f'images.txt')#要保存的model的images.txt
    if os.path.exists(i_path):
        os.remove(i_path)
      
    f=open(posefile)#时间戳位姿,posefile
    pose=list(f)
    f.close

    for i in tqdm(range(len(pose))):
                       
        with open(i_path, 'a') as f:
            str_dof=pose[i].split(' ')    
            name=str_dof[0]+'.jpg'#可能需要改成jpg等其他格式，视具体情况而定    
            qw = float(str_dof[7])        
            qx = float(str_dof[4])
            qy = float(str_dof[5])
            qz = float(str_dof[6])

            tx = float(str_dof[1])-368516
            ty = float(str_dof[2])-3459036
            tz = float(str_dof[3])-15

            r = R.from_quat([qx,qy,qz,qw])
            rotation = r.as_matrix()
    
            translation = np.asarray([tx,ty,tz])
            xyz = -np.dot(np.linalg.inv(rotation),translation)
            xyz = np.reshape(xyz,(1,3))
    
            r = R.from_matrix(np.linalg.inv(rotation))
            r2=r.as_quat()
    

            k=i+1
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
            
                

    #创建cameras.txt

    cameras_path=Path(emptySfM_path , f'cameras.txt')
    if os.path.exists(cameras_path):
        os.remove(cameras_path)
    
    camera_type='PINHOLE'

    with open(cameras_path, 'a') as f:
        #middle_front
        line='1'+' '
        line+=camera_type+' '
        line+='1920'+' '
        line+='1200'+' '
        line+='1077.319838'+' '+'1076.431366'+' '#fx fy
        line+='959.747465'+' '+'600.50007'#x0 y0
        f.write(line)



    #创建points3D.txt
    points3d_path  =  Path(emptySfM_path , f'points3D.txt')
    if os.path.exists(points3d_path):
        os.remove(points3d_path)
    open(points3d_path,'w')
    print("Finished create_emptySfM")

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

                # if posefile.split('/')[-1]=='cam03_2to1.txt':
                #     line+="1"+' '
                # elif posefile.split('/')[-1]=='cam05_2to1.txt':
                #     line+="2"+' '
                # elif posefile.split('/')[-1]=='cam06_2to1.txt':
                #     line+="3"+' '
                # elif posefile.split('/')[-1]=='cam07_2to1.txt':
                #     line+="4"+' '
                # elif posefile.split('/')[-1]=='cam08_2to1.txt':
                #     line+="5"+' '
                # else:
                #     print('something error')

                if posefile.split('/')[-1]=='front_left_10to1.txt':
                    line+="1"+' '
                elif posefile.split('/')[-1]=='front_center_10to1.txt'or posefile.split('/')[-1]=='fc_07_3to1.txt':
                    line+="2"+' '
                elif posefile.split('/')[-1]=='front_right_10to1.txt'or posefile.split('/')[-1]=='fr_07_3to1.txt':
                    line+="3"+' '
                elif posefile.split('/')[-1]=='fl_07_3to1.txt':
                    line+="4"+' '
                
                else:
                    print('something error')
            
                # line+='1'+' '
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

        # #cam03
        # line='1'+' '
        # line+=camera_type+' '
        # line+='1920'+' '
        # line+='1020'+' '
        # line+='1938.34597'+' '+'1937.09807'+' '#fx fy
        # line+='959.5'+' '+'509.5'#x0 y0
        # f.write(line+'\n')
        # #cam05
        # line='2'+' '
        # line+=camera_type+' '
        # line+='1920'+' '
        # line+='1020'+' '
        # line+='956.1788'+' '+'957..3191'+' '#fx fy
        # line+='942.1158'+' '+'534.9691'#x0 y0
        # f.write(line+'\n')
        # #cam06
        # line='3'+' '
        # line+=camera_type+' '
        # line+='1920'+' '
        # line+='1020'+' '
        # line+='960.2269'+' '+'961.1119'+' '#fx fy
        # line+='931.0223'+' '+'527.5472'#x0 y0
        # f.write(line+'\n')
        # #cam07
        # line='4'+' '
        # line+=camera_type+' '
        # line+='1920'+' '
        # line+='1020'+' '
        # line+='958.677'+' '+'959.2314'+' '#fx fy
        # line+='944.9455'+' '+'541.0408'#x0 y0
        # f.write(line+'\n')
        # #cam08
        # line='5'+' '
        # line+=camera_type+' '
        # line+='1920'+' '
        # line+='1020'+' '
        # line+='961.4182'+' '+'961.5139'+' '#fx fy
        # line+='933.085'+' '+'538.4962'#x0 y0
        # f.write(line+'\n')




    #创建points3D.txt
    points3d_path  =  Path(emptySfM_path , f'points3D.txt')
    if os.path.exists(points3d_path):
        os.remove(points3d_path)
    open(points3d_path,'w')
    print("Finished create_emptySfM")
# image_path='/media/autolab/disk_3T/caiyingfeng/huawei/0808/B1/front_5to1'
# base_path='/media/autolab/disk_4T/cyf/hw/camera_pose/database/'
# posefiles=[base_path+'cam03_2to1.txt',base_path+'cam05_2to1.txt',base_path+'cam06_2to1.txt',base_path+'cam07_2to1.txt',base_path+'cam08_2to1.txt']

# base_path='/media/autolab/disk_3T/caiyingfeng/huawei/10to1_gt/'
# posefiles=[base_path+'fl_08.txt',base_path+'fc_08.txt',base_path+'fr_08.txt',base_path+'fl_07_3to1.txt',base_path+'fc_07_3to1.txt',base_path+'fr_07_3to1.txt']

base_path='/media/autolab/disk_3T/caiyingfeng/huawei/0808/B1/gt/fusion_v10/'
posefiles=[base_path+'front_center_10to1.txt',base_path+'front_left_10to1.txt',base_path+'front_right_10to1.txt']
emptySfM_path='/media/autolab/disk_4T/cyf/localization/Herarchical-Localization/outputs/wanguo/sfm_empty_10to1_fusion_v10'
# posefile='/media/autolab/disk_3T/caiyingfeng/huawei/0808/B1/gt/front_center_5to1.txt'
# create_emptySfM_multi(image_path,posefiles,emptySfM_path)
# create_emptySfM(posefile,emptySfM_path)

# base_path='/media/autolab/disk_3T/caiyingfeng/huawei/'
# # posefiles=[base_path+'front_center_p0.txt',base_path+'front_center_r0.txt',base_path+'front_center_y0.txt',base_path+'front_center_original.txt']
# posefiles=[base_path+'Old_August_Lidar.txt']
# emptySfM_path='/media/autolab/disk_4T/cyf/localization/Herarchical-Localization/outputs/lidar/xyz_sfm_empty_old_august_cameratype_down'
create_emptySfM_threecam(posefiles,emptySfM_path)
