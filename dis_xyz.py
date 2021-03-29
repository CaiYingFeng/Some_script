import os
import numpy as np
import heapq
from scipy.spatial.transform import Rotation as R
# from data_gen.rotation import *

eval_name='0711_front_right_20to1_v12_BA'
gt_name='0711_front_right_20to1_fusion_v12_delete'
#评估位移用c2w
gt_path='/media/autolab/disk_4T/cyf/localization/out/eval/aachen/'+gt_name+'.txt'
estimate_path='/media/autolab/disk_4T/cyf/localization/out/eval/aachen/'+eval_name+'/poses_c2w.txt'

f=open(gt_path)
gt=list(f)
# gt=gt[50:]

f=open(estimate_path)
estimate=list(f)
# estimate=estimate[50:]

dis=[]
name=[]
for i in range(len(gt)):
    p1=gt[i].split(' ')
    p2=estimate[i].split(' ')
    # d=np.sum((float(p1[1])-float(p2[1]))**2+(float(p1[2])-float(p2[2]))**2+(float(p1[3])-float(p2[3]))**2)
    d=np.sum((float(p1[1])-float(p2[1]))**2+(float(p1[2])-float(p2[2]))**2)
    d=np.sqrt(d)
    dis.append(d)
    name.append(p1[0])

# dis = heapq.nlargest(600, dis)
# dis = heapq.nsmallest(550, dis)#删掉误差前50
print('位置误差')
print('mean: '+str(np.mean(dis)))
print('median: '+str(np.median(dis)))
print('max: '+str(np.max(dis)))
print('min: '+str(np.min(dis)))

# distance_thr=[0.1,0.25,0.5,1,2,3,5,10,30,50,100]
distance_thr=[0.5,1]
for my_dis in distance_thr:

    num_1=sum(i < my_dis for i in dis)#小于1m数量
    print('<'+str(my_dis)+'m: '+str(num_1)+'  '+str(100*num_1/len(gt)))
print("***********************************")
#评估角度
def angle_error(angle1,angle2):#angle:c2w的四元数，qx qy qz qw

    qx1=angle1[0]
    qy1=angle1[1]
    qz1=angle1[2]
    qw1=angle1[3]
    r1 = R.from_quat([qx1,qy1,qz1,qw1])
    rotation1 = r1.as_matrix()    
    o1o=np.array([rotation1[0][2],rotation1[1][2],rotation1[2][2]])

    qx2=angle2[0]
    qy2=angle2[1]
    qz2=angle2[2]
    qw2=angle2[3]
    r2 = R.from_quat([qx2,qy2,qz2,qw2])

    rotation2 = r2.as_matrix()
    o2o=np.array([rotation2[0][2],rotation2[1][2],rotation2[2][2]])

    cos_theta=np.dot(o1o,o2o)/(np.linalg.norm(o1o)*np.linalg.norm(o2o))
    if cos_theta>1:
        cos_theta=1
    
    theta=np.arccos(cos_theta)
    err=theta*180/np.pi

    return abs(err)

    # return np.arccos(np.dot(angle1,angle2))

#评估角度用w2c

angle_err=[]
for i in range(len(gt)):
    a1=gt[i].split(' ')
    a2=estimate[i].split(' ')
    angle1=[float(a1[4]),float(a1[5]),float(a1[6]),float(a1[7])]
    angle2=[float(a2[4]),float(a2[5]),float(a2[6]),float(a2[7])]
    angle_err.append(angle_error(angle1,angle2))



# angle_err = heapq.nlargest(600, angle_err)
# angle_err = heapq.nsmallest(550, angle_err)
print('角度误差')
print('mean: '+str(np.mean(angle_err)))
print('median: '+str(np.median(angle_err)))
print('max: '+str(np.max(angle_err)))
print('min: '+str(np.min(angle_err)))

# angle_thr=[0.1,0.5,1,2,3,5,10,20,30,50,90]
angle_thr=[3,5]
for my_angle in angle_thr:
    num=sum(i < my_angle for i in angle_err)#小于x°数量
    print('<'+str(my_angle)+'°: '+str(num)+'  '+str(100*num/len(gt)))


err_file='/media/autolab/disk_4T/cyf/localization/out/eval/aachen/'+eval_name+'/err_file.txt'
with open(err_file,'w') as f:
    for i in range(len(dis)):

        f.write(name[i]+" "+str(dis[i])+" "+str(angle_err[i])+'\n')
print("***********************************")
def get_percent(r,t,Thr_angle,Thr_tra):
    count=0
    for i in range(len(r)):
        if r[i]<Thr_angle and t[i]<Thr_tra:
            count+=1
    percent=100*count/len(r)
    return percent


r=angle_err
t=dis
if(len(distance_thr)==len(angle_thr)):
    for i in range(len(distance_thr)):
        Thr_tra=distance_thr[i]
        Thr_angle=angle_thr[i]
        # print(str(Thr_tra)+'米 '+str(Thr_angle)+'度：'+str(get_percent(r,t,Thr_angle,Thr_tra)))

Thr_tra=0.5
Thr_angle=3
print(str(Thr_tra)+'米 '+str(Thr_angle)+'度：'+str(get_percent(r,t,Thr_angle,Thr_tra)))

Thr_tra=1
Thr_angle=5
print(str(Thr_tra)+'米 '+str(Thr_angle)+'度：'+str(get_percent(r,t,Thr_angle,Thr_tra)))

# Thr_tra=2
# Thr_angle=5
# print(str(Thr_tra)+'米 '+str(Thr_angle)+'度：'+str(get_percent(r,t,Thr_angle,Thr_tra)))

# Thr_tra=2.5
# Thr_angle=5
# print(str(Thr_tra)+'米 '+str(Thr_angle)+'度：'+str(get_percent(r,t,Thr_angle,Thr_tra)))