import matplotlib.pyplot as plt
import time
import os
import sys
import tty
import termios
# cam='cam03_sp'
# f=open('/media/autolab/disk_4T/cyf/localization/out/eval/aachen/'+cam+'/'+'cam03.txt')
# f=open('/media/autolab/disk_4T/cyf/localization/out/eval/aachen/0808_front_center50to1.txt')
f=open('/media/autolab/disk_3T/caiyingfeng/huawei/0808/B1/gt/fusion_v5/front_center_10to1.txt')
# f=open('/media/autolab/disk_3T/caiyingfeng/huawei/LidarPose.txt')
# f=open('/media/autolab/disk_3T/caiyingfeng/huawei/0808/B1/gt/fusion_v10/front_center_10to1.txt')
gt_dof=list(f)
f.close

# f=open('/media/autolab/disk_4T/cyf/localization/out/eval/aachen/fc_20to1_fusion_v5/poses_c2w.txt')
f=open('/media/autolab/disk_4T/cyf/localization/out/eval/aachen/0711_front_center_20to1_fusion_delete.txt')
# f=open('/media/autolab/disk_3T/caiyingfeng/huawei/0711/F1/gt/fusion_v5/front_center.txt')
gt_dof_0711=list(f)
f.close

# # f=open('/media/autolab/disk_4T/cyf/localization/out/eval/aachen/'+cam+'/estimate.txt')
# f=open('/media/autolab/disk_4T/cyf/localization/out/eval/aachen/fc_20to1-front_10to1_spatialplus_15_0.5_70/estimate.txt')
# result_dof=list(f)
# f.close


# plt.ion()
ground_x = []
ground_y = []
ground_x1 = []
ground_y1 = []
dx_ground_x1 = []
dy_ground_y1 = []

ground_x_0711 = []
ground_y_0711 = []
dx_ground_x_0711 = []
dy_ground_y_0711 = []

result_x = []
result_y = []
  

def plt_points():
    global plt
    
    if  True:
        plt.cla()

        # plt.scatter(ground_x, ground_y, s=5, c='r', label="ground truth")
        plt.scatter(ground_x1, ground_y1, s=8, c='b', label="ground truth")
        # plt.plot(ground_x1, ground_y1, c='b', label="db ground truth")
        # plt.arrow(ground_x1, ground_y1, dx_ground_x1, dy_ground_y1)
        # plt.scatter(ground_x_0711, ground_y_0711, s=12,c='g',marker='X', label="query ground truth")
        plt.plot(ground_x_0711, ground_y_0711, c='r', label="query ground truth")
        # plt.scatter(result_x, result_y, c='g', label="result pose")

        plt.legend()
    plt.pause(0.00001)  
    # os.system("pause") 


for i in range(0,len(gt_dof)):
    # for i in range(4000,len(gt_dof),10):
    ground_x1.append(float(gt_dof[i].split()[1]))
    ground_y1.append(float(gt_dof[i].split()[2]))
    if i ==len(gt_dof)-1:
        dx_ground_x1.append(0)
        dy_ground_y1.append(0)
    else:
        dx_ground_x1.append(float(gt_dof[i+1].split()[1])-float(gt_dof[i].split()[1]))
        dy_ground_y1.append(float(gt_dof[i+1].split()[2])-float(gt_dof[i].split()[2])) 
# plt.plot(ground_x1, ground_y1, c='b', label="db ground truth")    
    # plt_points()
# plt.plot(ground_x1, ground_y1, c='b', label="0808")
for i in range(0,len(gt_dof),10):
    plt.arrow(ground_x1[i],ground_y1[i],dx_ground_x1[i],dy_ground_y1[i],width=0.01,head_width=3,fc='blue',ec='black')
plt.legend()
# plt.show()  

    
for i in range(len(gt_dof_0711)):
# for i in range(430,460):
    ground_x_0711.append(float(gt_dof_0711[i].split()[1]))
    ground_y_0711.append(float(gt_dof_0711[i].split()[2]))
    if i ==len(gt_dof_0711)-1:
        dx_ground_x_0711.append(0)
        dy_ground_y_0711.append(0)
    else:
        dx_ground_x_0711.append(float(gt_dof_0711[i+1].split()[1])-float(gt_dof_0711[i].split()[1]))
        dy_ground_y_0711.append(float(gt_dof_0711[i+1].split()[2])-float(gt_dof_0711[i].split()[2]))
# plt.plot(ground_x_0711, ground_y_0711, c='r', label="query ground truth")
for i in range(0,len(gt_dof_0711)):
    plt.arrow(ground_x_0711[i],ground_y_0711[i],dx_ground_x_0711[i],dy_ground_y_0711[i],width=0.001,head_width=2,fc='red',ec='black')
plt.show()

# plt_points()
# plt.plot(ground_x, ground_y, c='r', label="0711 query")
# plt.legend()
# plt.show()  




# for i in range(len(gt_dof)):

       
#     ground_x.append(float(gt_dof[i].split()[1]))
#     ground_y.append(float(gt_dof[i].split()[2]))
# plt_points()
# plt.plot(ground_x, ground_y, c='r', label="0808")
# plt.legend()
# # plt.show()
# for i in range(len(result_dof)):
# # for i in range(600):

#     # ground_x.append(float(gt_dof[i].split(' ',-1)[1]))
#     # ground_y.append(float(gt_dof[i].split(' ',-1)[2]))
#     result_x.append(float(result_dof[i].split(' ',-1)[1]))
#     result_y.append(float(result_dof[i].split(' ',-1)[2]))

    # plt_points()
print('finished')
# plt.pause(20)
# plt.close()
