
# # cams=['front_center','front_left','front_right']
cams=['front_center']
for cam in cams:
    # count=0
    for i in range(0,7):
        time_stamp_path='/media/autolab/disk_3T/caiyingfeng/huawei/0711/F1/name_pose/'+str(i)+'_'+cam+'.txt'
        dof_path='/media/autolab/disk_3T/caiyingfeng/6DOF/0711SC/F1/'+str(i)+'_camera_'+cam+'.txt'
        gt_path='/media/autolab/disk_3T/caiyingfeng/huawei/0711/F1/gtsc/'+str(i)+'_'+cam+'.txt'
        time_stamp=open(time_stamp_path)
        time_stamp_list=list(time_stamp)

        dof=open(dof_path)
        dof_list=list(dof)
        # num=len(dof_list)
        # num=len(time_stamp_list)
        # print(num)
        # count+=num
    # print(count)
        with open(gt_path,'w') as f:
            assert len(dof_list)==len(time_stamp_list)
            for i in range(len(time_stamp_list)):
                f.write(time_stamp_list[i].strip('\n')+' '+dof_list[i].split(' ',1)[1])

# with open('/media/autolab/disk_4T/cyf/localization/Herarchical-Localization/pairs/huawei/2to1_10_0.5_36.txt') as f:
#     for line in f.readlines():
#         with open('/media/autolab/disk_4T/cyf/localization/Herarchical-Localization/pairs/huawei/2to1_10_0.5_36_.txt',"a") as fp:
#             fp.write(line.replace('.jpg','.png'))            


