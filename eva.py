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
    # d=np.sum((float(p1[0])-float(p2[0]))**2+(float(p1[1])-float(p2[1]))**2+(float(p1[2])-float(p2[2]))**2)
    d=np.sum((float(p1[0])-float(p2[0]))**2+(float(p1[1])-float(p2[1]))**2)
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
    




def angle_error(angle1,angle2):#angle:相机到世界的四元数，qw qx qy qz
    qx1=angle1[1]
    qy1=angle1[2]
    qz1=angle1[3]
    qw1=angle1[0]
    r1 = R.from_quat([qx1,qy1,qz1,qw1])
    # rotation1 = r1.as_matrix()
    rotation1=np.linalg.inv(rotation1)
    o1o=np.array([rotation1[0][2],rotation1[1][2],rotation1[2][2]])


    qx2=angle2[1]
    qy2=angle2[2]
    qz2=angle2[3]
    qw2=angle2[0]
    r2 = R.from_quat([qx2,qy2,qz2,qw2])

    rotation2 = r2.as_matrix()
    # rotation2=np.linalg.inv(rotation2)
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





gt_pose_filepath='/media/autolab/disk_3T/caiyingfeng/huawei/0808/B1/gt/front_center.txt'
est_pose_filepath='/media/autolab/disk_4T/cyf/localization/out/eval/aachen/fc_20to1-front_10to1_spatialplus_15_0.5_70/estimate_z=0.txt'
est_pose_filepath='/media/autolab/disk_4T/cyf/localization/out/eval/aachen/0711_front_center20to1_align2.txt'

gt_pose_file=open(gt_pose_filepath)
est_pose_file=open(est_pose_filepath)
gt=list(gt_pose_file)#c2w: time x y z qx qy qz qw
est=list(est_pose_file)#c2w: time x y z qx qy qz qw

gt_pose=[]
gt_xyz=[]
gt_angle=[]
est_pose=[]
est_xyz=[]
est_angle=[]

dis_er=[]
angle_er=[]


for i in range(len(gt)):
    gt_str=gt[i].strip('/n').split(' ')
    # gt_xyz.append([float(gt_str[1]),float(gt_str[2]),float(gt_str[3])])#x y z
    gt_xyz.append([float(gt_str[1]),float(gt_str[2]),0])#x y 0
    gt_angle.append([float(gt_str[4]),float(gt_str[5]),float(gt_str[6]),float(gt_str[7])])#qx qy qz qw

for i in range(len(est)):
    est_str=est[i].strip('/n').split(' ')
    # est_xyz.append([float(est_str[1]),float(est_str[2]),float(est_str[3])])#x y z
    est_xyz.append([float(est_str[1]),float(est_str[2]),0])#x y 0
    est_angle.append([float(est_str[4]),float(est_str[5]),float(est_str[6]),float(est_str[7])])#qx qy qz qw


Thr_dis=1#距离阈值
knn = NearestNeighbors()
knn.fit(gt_xyz)#db
# distances, positives = knn.radius_neighbors(est_xyz, radius=Thr_dis)#query
distances, positives =knn.kneighbors(est_xyz, n_neighbors=10)

dis_er=distances[:,0]
print(np.median(dis_er))


