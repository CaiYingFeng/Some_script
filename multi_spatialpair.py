import os
import numpy as np
import heapq
from scipy.spatial.transform import Rotation as R
from sklearn.neighbors import NearestNeighbors
from tqdm import tqdm
from multiprocessing import Pool
from multiprocessing import Process
import multiprocessing
import math
def dis(p1,p2):
    d=np.sum((float(p1[0])-float(p2[0]))**2+(float(p1[1])-float(p2[1]))**2+(float(p1[2])-float(p2[2]))**2)
    d=np.sqrt(d)

    return d

def pairs(pairs_filepath, positives,pose_t,s_index, e_index, thread_name):
    pairs=[]
    for i in range(s_index,e_index):
        # if (i-s_index)!=0 and (i-s_index)%500==0:
        #     print(thread_name+':'+str(i-s_index)+'/'+str(e_index-s_index+1))
        
        pair=[]
        
        my_d=[]
        for j in range(len(positives[i])):
            flag=False           
            for k in range(len(pair)):
                d=dis(pose_t[pair[k][1]],pose_t[positives[i][j]])
                if d<Thr_filter:
                    flag=True#表明现有pair里已经有一对了
                    break
            if not flag:
                pair.append([i,positives[i][j]])
        # print(len(pair))
        pairs+=pair
    # print(len(pairs)/len(pose_t))
    count=0
    err_list=[]
    with open(pairs_filepath+'_'+thread_name+'.txt','w') as f:

        for i , j in pairs:  
            err=angle_error(pose_q[i],pose_q[j])
            err_list.append(err)
            if err<Thr_angle:
                count+=1
                
                f.write(name[i+1]+' '+name[j+1]+'\n')
    print('thread '+thread_name+' finished!')
    # print(max(err_list))
    # print(count)
    # print(count/len(pose_t))
    




def angle_error(angle1,angle2):#angle:世界到相机的四元数，qw qx qy qz
    qx1=angle1[1]
    qy1=angle1[2]
    qz1=angle1[3]
    qw1=angle1[0]
    r1 = R.from_quat([qx1,qy1,qz1,qw1])
    rotation1 = r1.as_matrix()
    rotation1=np.linalg.inv(rotation1)
    o1o=np.array([rotation1[0][2],rotation1[1][2],rotation1[2][2]])


    qx2=angle2[1]
    qy2=angle2[2]
    qz2=angle2[3]
    qw2=angle2[0]
    r2 = R.from_quat([qx2,qy2,qz2,qw2])

    rotation2 = r2.as_matrix()
    rotation2=np.linalg.inv(rotation2)
    o2o=np.array([rotation2[0][2],rotation2[1][2],rotation2[2][2]])

    
    cos_theta=np.dot(o1o,o2o)/(np.linalg.norm(o1o)*np.linalg.norm(o2o))
    if cos_theta>1:    
        # print(cos_theta)
        cos_theta=1
    if cos_theta<-1:    
        # print(cos_theta)
        cos_theta=-1
    theta=np.arccos(cos_theta)
    err=theta*180/np.pi

    return err




Thr_dis=10#距离阈值
Thr_filter=0.5#间隔xm取一个
Thr_angle=70#角度阈值
K_N=100
outfile='11fusion_8-7_10to1_'+str(Thr_dis)+'_'+str(Thr_filter)+'_'+str(Thr_angle)#输出pairs的txt名

pose_filepath='/media/autolab/disk_4T/cyf/localization/Herarchical-Localization/outputs/wanguo/sfm_empty_10to1_fusion_8-7/images.txt'#w2c
pairs_filepath='/media/autolab/disk_4T/cyf/localization/Herarchical-Localization/pairs/wanguo/'+outfile
pose_file=open(pose_filepath)
p=list(pose_file)#image_id qw,qx,qy,qz,tx,ty,tz cameraid image_name
pose=[]
pose_t=[]
pose_q=[]
name={}


for i in range(0,len(p),2):
# for i in index:
    str_pose=p[i].split(' ')
    image_id=int(str_pose[0])
    image_name=str_pose[9].strip('\n')
    
    qw=float(str_pose[1])
    qx=float(str_pose[2])
    qy=float(str_pose[3])
    qz=float(str_pose[4])
    tx=float(str_pose[5])
    ty=float(str_pose[6])
    tz=float(str_pose[7])

    r = R.from_quat([qx,qy,qz,qw])#把xyz转到c2w
    rotation = r.as_matrix()  
    translation = np.asarray([tx,ty,tz])
    xyz = -np.dot(np.linalg.inv(rotation),translation)
    xyz = np.reshape(xyz,(1,3))

    pose.append([image_name,qw,qx,qy,qz,tx,ty,tz])
    pose_t.append(xyz[0].tolist())#算位置距离用c2w
    pose_q.append([qw,qx,qy,qz])#算角度误差用w2c
    name.update({image_id:image_name})


knn = NearestNeighbors()
knn.fit(pose_t)#db
# distances, positives =knn.kneighbors(pose_t)
distances, positives = knn.radius_neighbors(pose_t, radius=Thr_dis)#query
num_thread=8
index=math.floor(len(positives)/num_thread)
pool = multiprocessing.Pool(processes=num_thread)

for i in range(num_thread):
    if i<num_thread-1:
        pool.apply_async(pairs,(pairs_filepath, positives,pose_t, index*i, index*(i+1),str(i)))
    elif i==num_thread-1:
        pool.apply_async(pairs,(pairs_filepath, positives,pose_t, index*i, len(positives),str(i)))

pool.close()
pool.join()

for i in range(num_thread):
    with open(pairs_filepath+'_'+str(i)+'.txt') as f:
        for line in f.readlines():
            with open(pairs_filepath+'.txt',"a") as fp:
                fp.write(line)
    os.remove(pairs_filepath+'_'+str(i)+'.txt')