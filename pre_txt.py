from scipy.spatial.transform import Rotation as R
import numpy as np
from pyquaternion import Quaternion
import matplotlib.pyplot as plt
# f=open('/media/autolab/disk_4T/cyf/localization/out/eval/aachen/fc_20to1-front_10to1_spatialplus_15_0.5_70/estimate.txt')#time tx ty tz qx qy qz qw
f=open('/media/autolab/disk_3T/caiyingfeng/huawei/0711/F1/gt/front_right.txt')
# f=open('/media/autolab/disk_4T/cyf/localization/out/eval/aachen/0711_front_center_20to1_lidaralign.txt')
gt_dof=list(f)
f.close

gt_x_07=[]
gt_y_07=[]
gt_x_8=[]
gt_y_8=[]

# gt_path='/media/autolab/disk_4T/cyf/localization/out/eval/aachen/0711_front_center20to1_align2.1_3.2.txt'
gt_path='/media/autolab/disk_3T/caiyingfeng/huawei/0711/F1/gt/front_right_align.txt'
for i in range(0,len(gt_dof)):               
        str_dof=gt_dof[i].split(' ',-1)
        with open(gt_path, 'a') as f:
            time=str_dof[0]
            qw = float(str_dof[7])        
            qx = float(str_dof[4])
            qy = float(str_dof[5])
            qz = float(str_dof[6])
            
            tx = float(str_dof[1])-368496
            ty = float(str_dof[2])-3459040
            # tx = float(str_dof[1])
            # ty = float(str_dof[2])
            # tz = float(str_dof[3])
            tz=0

            r = R.from_quat([qx,qy,qz,qw])
            rotation = r.as_matrix()
            translation = np.asarray([tx,ty,tz])
            T=np.eye(4)
            T[:3,:3]=rotation
            T[:3,3]=translation

            trans=np.array([[0.999488,-0.0319945,0,2.5],[0.0319945,0.999488,0,3],[0,0,1,0],[0,0,0,1]])#总体
            # trans=np.array([[-0.274312,-0.029167,0.961199,368497.968750],[0.961627,-0.002952,0.274344,3459044.750000],[-0.005164,0.999570, 0.028857, 16.361328],[0,0,0,1.0]])
            # trans=np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
            query_T_w=np.dot(trans,T)
            qvec_nvm = list(Quaternion(matrix=query_T_w))
            pos_nvm = query_T_w[:3, 3].tolist()
            # pos_nvm=np.dot(trans,translation)
            
            pos_nvm[0]=pos_nvm[0]+368496
            pos_nvm[1]=pos_nvm[1]+3459040
            line = time+' '
            gt_x_07.append(pos_nvm[0])
            gt_y_07.append(pos_nvm[1])

            line +=' '.join(str(i) for i in pos_nvm)
            line +=' '+str(qvec_nvm[1])
            line +=' '+str(qvec_nvm[2])
            line +=' '+str(qvec_nvm[3])
            line +=' '+str(qvec_nvm[0])

            f.write(line+'\n')


# with open(gt_path, 'w') as f:
#     for i in range(len(gt_dof)):
#         s=gt_dof[i].split(' ')
#         s[3]=str(0)
#         line=' '.join(s)
#         f.write(line)



f=open('/media/autolab/disk_4T/cyf/localization/out/eval/aachen/0808_front_left50to1.txt')
gt_list_8=list(f)
f.close
for i in range(len(gt_list_8)):
    # for i in range(20000,30000):
    gt_x_8.append(float(gt_list_8[i].split()[1]))
    gt_y_8.append(float(gt_list_8[i].split()[2]))
# plt.scatter(gt_x_7, gt_y_7, c='g', label="0711")
plt.plot(gt_x_8, gt_y_8, c='r', label="0808")
plt.plot(gt_x_07, gt_y_07, c='b', label="0711")

plt.legend()
plt.show()

# est_path='/media/autolab/disk_4T/cyf/localization/out/eval/aachen/0711_front_center_20to1_lidaralign_z=0.txt'

# result_dof=list(open('/media/autolab/disk_4T/cyf/localization/out/eval/aachen/0711_front_center_20to1_lidaralign.txt'))    
# with open(est_path, 'w') as f:
#     for i in range(len(result_dof)):
#         s=result_dof[i].split(' ')
#         s[3]=str(0)
#         line=' '.join(s)
#         f.write(line)