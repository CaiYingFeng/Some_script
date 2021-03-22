import sqlite3
import os
from pathlib import Path
import numpy as np
from pyquaternion import Quaternion
from scipy.spatial.transform import Rotation as R
import argparse
import logging
import subprocess
import sys
import numpy as np
IS_PYTHON3 = sys.version_info[0] >= 3
def array_to_blob(array):
    if IS_PYTHON3:
        return array.tostring()
    else:
        return np.getbuffer(array)
def blob_to_array(blob, dtype, shape=(-1,)):
    if IS_PYTHON3:
        return np.fromstring(blob, dtype=dtype).reshape(*shape)
    else:
        return np.frombuffer(blob, dtype=dtype).reshape(*shape)

def create_emptySfM( posefile , emptySfM_path ,db_path ):
    print("Running create_emptySfM")

#posefile:时间戳位姿文件，每行为 time tx ty tz qx qy qz qw ；time必须与图片同名（除后缀名）,eg:$pro/pose.txt
#emptySfM:要存放的空SfM模型，一个文件夹，eg:$pro/emptySfM
#dbpath:特征点存放的位置，eg:$pro/database.db文件  
    if not os.path.exists(emptySfM_path):
            os.makedirs(emptySfM_path)
   
    # f=open('/media/autolab/disk_4T/cyf/hw/camera_pose/database/database_pose_sorted.txt')#时间戳位姿,posefile
    f=open(posefile)#时间戳位姿,posefile
    f_dof=list(f)
    f.close

    # i_path=Path('/media/autolab/disk_4T/cyf/map/model',f'images.txt')#要保存的model的images.txt
    # if os.path.exists('/media/autolab/disk_3T/caiyingfeng/map/model/images.txt'):
    #     os.remove('/media/autolab/disk_3T/caiyingfeng/map/model/images.txt')


    #创建images.txt
    i_path=Path(emptySfM_path , f'images.txt')#要保存的model的images.txt
    if os.path.exists(i_path):
        os.remove(i_path)
    conn = sqlite3.connect(db_path)#特征点保存的数据库
    cursor = conn.cursor()
    sql = """select * from images"""

    cursor.execute(sql) 
    result = cursor.fetchall()#result[i][1]表示id=i的图片的name
    # print(len(result))


    for i in range(0,len(result)):
        
        for j in range(0,len(f_dof)):
            str_dof=f_dof[j].split(' ',-1)
            name=str_dof[0]+'.png'#可能需要改成jpg等其他格式，视具体情况而定

            if name==result[i][1]:            
                
                with open(i_path, 'a') as f:

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

                    # line+="1"+' '+'db/'
                    line+="1"+' '
                    line+=name.__str__()
                        
                    f.write(line+'\n'+'\n')
                break

    #创建cameras.txt
    sql = """select * from cameras"""
    cursor.execute(sql) 
    result = cursor.fetchall()

    cameras_path=Path(emptySfM_path , f'cameras.txt')
    if os.path.exists(cameras_path):
        os.remove(cameras_path)
    camera_type=''
    if result[0][1]==1:
        camera_type='PINHOLE'
    elif result[0][1]==0:
        camera_type='SIMPLE_PINHOLE'

    with open(cameras_path, 'a') as f:
        line='1'+' '
        line+=camera_type+' '
        line+=result[0][2].__str__()+' '
        line+=result[0][3].__str__()+' '
        line+='1938.34'+' '+'1937.10'+' '
        line+='959.5'+' '+'509.5'
        # line+=(result[0][3]/(result[0][2])*960.0).__str__()
        # line+=result[0][4].__str__()

        f.write(line)
    conn.close()

    #创建points3D.txt
    points3d_path  =  Path(emptySfM_path , f'points3D.txt')
    if os.path.exists(points3d_path):
        os.remove(points3d_path)
    open(points3d_path,'w')
    print("Finished create_emptySfM")


def update_database(emptySfM_path , database_path):
    print("Running update_database")
    f = open(emptySfM_path+"/images.txt","r")#id,qw,qx,qy,qz,tx,ty,tz,cid,name
    dof=list(f)
    f.close
    f_dof=list()
    for i in range(0,len(dof),2):
        f_dof.append(dof[i])

    
    conn = sqlite3.connect(database_path)#db文件地址
    cursor = conn.cursor()
    sql = """select * from images"""

    cursor.execute(sql)
    result = cursor.fetchall()#result[i][1]表示id=i的图片的name

    
    for i in range(0,len(result)):#len(result)
        #print(i)
        str_dof=f_dof[i].split(' ',-1)
        str_name=str_dof[9].strip('\n')
        myqw=float(str_dof[1])
        myqx=float(str_dof[2])
        myqy=float(str_dof[3])
        myqz=float(str_dof[4])
        mytx=float(str_dof[5])
        myty=float(str_dof[6])
        mytz=float(str_dof[7])
        # print(str_name)
        # print(myqw,mytz)

        cursor.execute(
                "update images set prior_qw=?,prior_qx=?,prior_qy=?,prior_qz=?,prior_tx=?,prior_ty=?,prior_tz=? where name=?",
                (myqw,myqx,myqy,myqz,mytx,myty,mytz,str_name))
        
        conn.commit()  #提交，以保存执行结果
    

    #更新表cameras
    # cursor.execute('SELECT params FROM cameras WHERE camera_id=?;',
    #                 (1,))
    # data = cursor.fetchall()
    # intrinsics = blob_to_array(data[0][0], np.double)

    # intrinsics[0]=1938.34
    # intrinsics[1]=1937.10
    # intrinsics[2]=959.5
    # intrinsics[3]=509.5


    # cursor.execute('UPDATE cameras SET params = ?;',
    #                 [array_to_blob(intrinsics)])

        
    # conn.commit()  #提交，以保存执行结果


    conn.close()
    print("Finished update database")



def run_feature_extractor(colmap_path,  image_path, database_path, mask_path='',camera_model='PINHOLE'):
    print('Running the feature_extractor...')
    
    if mask_path=='':
        cmd = [
            str(colmap_path), 'feature_extractor',
            '--image_path', str(image_path),
            '--database_path', str(database_path),
            '--ImageReader.camera_model',str(camera_model) ,
            '--ImageReader.single_camera','1',
            '--ImageReader.camera_params','1938.34,1937.10,959.5,509.5'
            ]
    else:
        cmd = [
            str(colmap_path), 'feature_extractor',
            '--image_path', str(image_path),
            '--ImageReader.mask_path', str(mask_path),
            '--database_path', str(database_path),
            '--ImageReader.camera_model',str(camera_model),
            '--ImageReader.single_camera','1',
            '--ImageReader.camera_params','1938.34,1937.10,959.5,509.5'
            ]

        
    # logging.info(' '.join(cmd))
    print(cmd)
    ret = subprocess.call(cmd)
    if ret != 0:
        logging.warning('Problem with feature_extractor, exiting.')
        exit(ret)
    print('Finished the feature_extractor...')

def run_spatial_matcher(colmap_path,database_path):
    print('Running the spatial_matcher...')
    
    
    
    cmd = [
        str(colmap_path), 'spatial_matcher',
        '--database_path', str(database_path),
        '--SpatialMatching.is_gps','0'
        
        ]

        
    # logging.info(' '.join(cmd))
    print(cmd)
    ret = subprocess.call(cmd)
    if ret != 0:
        logging.warning('Problem with spatial_matcher, exiting.')
        exit(ret)

    print('Finished the spatial_matcher...')

def run_sequential_matcher(colmap_path,database_path):
    print('Running the spatial_matcher...')
    vocab_tree_path='/media/autolab/disk_3T/caiyingfeng/vocab_tree_flickr100K_words256K.bin'
    
    
    cmd = [
        str(colmap_path), 'sequential_matcher',
        '--database_path', str(database_path),
        '--SequentialMatching.vocab_tree_path', str(vocab_tree_path),
        '--SequentialMatching.loop_detection','1'

        
        ]

        
    # logging.info(' '.join(cmd))
    print(cmd)
    ret = subprocess.call(cmd)
    if ret != 0:
        logging.warning('Problem with sequential_matcher, exiting.')
        exit(ret)

    print('Finished the sequential_matcher...')

def run_triangulation(colmap_path, model_path, database_path, image_path, emptySfM_path):
    if not os.path.exists(model_path):
            os.makedirs(model_path)
    print('Running the triangulation...')
    

    cmd = [
        str(colmap_path), 'point_triangulator',
        '--database_path', str(database_path),
        '--image_path', str(image_path),
        '--input_path', str(emptySfM_path),
        '--output_path', str(model_path),
        # '--Mapper.ba_refine_focal_length', '0',
        # '--Mapper.ba_refine_principal_point', '0',
        # '--Mapper.ba_refine_extra_params', '0'
        ]
        
    # logging.info(' '.join(cmd))
    print(cmd)
    ret = subprocess.call(cmd)
    if ret != 0:
        logging.warning('Problem with point_triangulator, exiting.')
        exit(ret)

    print('Finished the triangulation...')

def run_BA(colmap_path, model_path, BA_model):
    if not os.path.exists(BA_model):
        os.makedirs(BA_model)
    print('Running bundle_adjuster...')
    

    cmd = [
        str(colmap_path), 'bundle_adjuster',

        '--input_path', str(model_path),
        '--output_path', str(BA_model)
        ]

    print(cmd)
    ret = subprocess.call(cmd)
    if ret != 0:
        logging.warning('Problem with bundle_adjuster, exiting.')
        exit(ret)

    print('Finished bundle_adjuster...')
    


if __name__ == "__main__":
    os.environ["CUDA_VISIBLE_DEVICES"] = "2,3"
    
    opts = argparse.ArgumentParser("This script is used to mapping.")
    opts.add_argument("--colmap_path", default='colmap')
    opts.add_argument("--image_path", default='/media/autolab/disk_4T/cyf/hw/database/cam03')#图片目录：需提供文件
    opts.add_argument("--posefile", default='/media/autolab/disk_4T/cyf/hw/camera_pose/database/cam03.txt')#图片位姿：需提供文件
    # opts.add_argument("--mask_path", default='/media/autolab/disk_4T/cyf/hw/mask/cam03')#只针对colmap的sift提取特征时图片掩码：可选提供
    opts.add_argument("--database_path", default='/media/autolab/disk_4T/cyf/map/cam03.db')#生成的数据库文件存放位置
    opts.add_argument("--emptySfM_path", default='/media/autolab/disk_4T/cyf/map/model')#生成的空SfM存放位置
    opts.add_argument("--model_path", default='/media/autolab/disk_4T/cyf/map/new_model')#生成的SfM模型
    opts.add_argument("--camera_model", default='PINHOLE')#相机模型
    opts.add_argument("--BA_model", default='/media/autolab/disk_4T/cyf/map/BA_model')#BA后模型存放

    # opts.add_argument("--image_path", default='/media/autolab/disk_4T/cyf/hw/query/cam03')#图片目录：需提供文件
    # opts.add_argument("--posefile", default='/media/autolab/disk_4T/cyf/hw/camera_pose/query/cam03.txt')#图片位姿：需提供文件
    opts.add_argument("--mask_path", default='')#只针对colmap的sift提取特征时图片掩码：可选提供
    # opts.add_argument("--database_path", default='/media/autolab/disk_4T/cyf/map/cam03.db')#生成的数据库文件存放位置
    # opts.add_argument("--emptySfM_path", default='/media/autolab/disk_4T/cyf/map/model')#生成的空SfM存放位置
    # opts.add_argument("--model_path", default='/media/autolab/disk_4T/cyf/localization/Herarchical-Localization/outputs/huawei/aslfeat/new_model')#生成的SfM模型
    # opts.add_argument("--camera_model", default='PINHOLE')#相机模型
    # opts.add_argument("--BA_model", default='/media/autolab/disk_4T/cyf/localization/Herarchical-Localization/outputs/huawei/aslfeat/BA_model')#BA后模型存放

    

    opts = opts.parse_args()

    colmap_path=opts.colmap_path
    image_path= opts.image_path
    posefile=opts.posefile
    mask_path=opts.mask_path
    database_path=opts.database_path
    emptySfM_path=opts.emptySfM_path
    model_path=opts.model_path #output model
    camera_model=opts.camera_model
    BA_model=opts.BA_model


    run_feature_extractor(colmap_path, image_path, database_path, mask_path, camera_model)   

    create_emptySfM(posefile , emptySfM_path ,database_path )

    update_database(emptySfM_path,database_path)

    # run_spatial_matcher(colmap_path,database_path)
    run_sequential_matcher(colmap_path,database_path)

    run_triangulation(colmap_path, model_path, database_path, image_path, emptySfM_path)

    run_BA(colmap_path, model_path, BA_model)


    

