import matplotlib.pyplot as plt

# gt_path_7='/media/autolab/disk_3T/caiyingfeng/huawei/0711/F1/gt/front_center.txt'#7月的gt
# gt_path_7='/media/autolab/disk_4T/cyf/localization/out/eval/aachen/0711_front_center20to1.txt'
gt_path_7='/media/autolab/disk_4T/cyf/localization/out/eval/aachen/fc_20to1-front_10to1_spatialplus_15_0.5_70/estimate_z=0.txt'
gt_list_7=list(open(gt_path_7))

gt_path_8='/media/autolab/disk_3T/caiyingfeng/huawei/0808/B1/gt/front_center.txt'
# gt_path_8='/media/autolab/disk_4T/cyf/localization/out/eval/aachen/mobile-up-down/poses_c2w.txt'
gt_list_8=list(open(gt_path_8))

gt_x_7=[]
gt_y_7=[]
gt_x_8=[]
gt_y_8=[]

for i in range(len(gt_list_7)):
    gt_x_7.append(float(gt_list_7[i].split()[1]))
    gt_y_7.append(float(gt_list_7[i].split()[2]))
for i in range(len(gt_list_8)):
# for i in range(20000,30000):
    gt_x_8.append(float(gt_list_8[i].split()[1]))
    gt_y_8.append(float(gt_list_8[i].split()[2]))
plt.plot(gt_x_7, gt_y_7, c='g', label="0711")
plt.plot(gt_x_8, gt_y_8, c='r', label="0808")
# plt.scatter(gt_x, gt_y, c='g', label="ground truth")
# plt.scatter(est_x, est_y, c='r', label="estimate")

plt.legend()
plt.show()