import os
#f=open('/media/autolab/disk_3T/caiyingfeng/rpg_trajectory_evaluation/front_left/stamped_groundtruth.txt')
f=open('/media/autolab/disk_3T/caiyingfeng/rpg_trajectory_evaluation/front_left_colmap/stamped_traj_estimate.txt')
groundtruth=list(f)
groundtruth.sort()
f.close()
# print(f_dof[0])
# print(len(f_dof))

f=open('/media/autolab/disk_3T/caiyingfeng/rpg_trajectory_evaluation/front_left/stamped_groundtruth.txt')
#f=open('/media/autolab/disk_3T/caiyingfeng/rpg_trajectory_evaluation/front_left_adjust_colmap/stamped_traj_estimate.txt')
estimate=list(f)
estimate.sort()
f.close()

# print(im_name[0])
# print(len(im_name))
i_path='/media/autolab/disk_3T/caiyingfeng/rpg_trajectory_evaluation/front_left_adjust_colmap/stamped_traj_estimate1.txt'
for i in range(0,len(estimate)):
    estimate_name=estimate[i].split(" ",-1)
    name=estimate_name[0]
    for j in range(0,len(groundtruth)):
        groundtruth_dof=groundtruth[j].split(" ",-1)
        g_name=groundtruth_dof[0]
        if(name==g_name):


            with open(i_path, 'a') as f:   
                line=name+' ' 
        
         
                line+=groundtruth_dof[1]+' '
                line+=groundtruth_dof[2]+' '
                line+=groundtruth_dof[3]+' '
                line+=groundtruth_dof[4]+' '
                line+=groundtruth_dof[5]+' '
                line+=groundtruth_dof[6]+' '
                line+=groundtruth_dof[7].strip("\n")+' ' 
                #print(line) 
                f.write(line+'\n')

