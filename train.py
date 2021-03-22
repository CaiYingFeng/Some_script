import os
from pathlib import Path
# str_name='front_center'
# f=open("/media/autolab/disk_3T/caiyingfeng/6DOF/0711/B1/"+str_name+".txt")#时间戳位姿
# f_dof=list(f)
# f_dof.sort()
# f.close
# dir_path = '/media/autolab/disk_3T/caiyingfeng/huawei/0711/F1/'+str_name
# image_name_list=os.listdir(dir_path)
# image_name_list.sort()


# f=open("/media/autolab/disk_3T/caiyingfeng/6DOF/0808/B1/front_right.txt")#时间戳位姿
# f_dof=list(f)
# f.close
# for k in range(3):

#     i_path=Path('/media/autolab/disk_3T/caiyingfeng/6DOF/0711/image_name/'+str_name+k.__str__()+'.txt')
#     for i in range(k,len(f_dof),3):
#         str_dof=f_dof[i].split(' ',-1)

#         with open(i_path, 'a') as f:
#             line=str_name+'/'+image_name_list[i]+' '       
                
#             line+=str_dof[1]+' '
#             line+=str_dof[2]+'\n'
#             f.write(line)


f=open("/media/autolab/disk_3T/caiyingfeng/rpg_trajectory_evaluation/front_center_0711/query_0711_groundtruth.txt")#时间戳位姿
f_dof=list(f)
f.close
i_path=Path('/media/autolab/disk_3T/caiyingfeng/pytorch-NetVlad/data/datasets/query_0711.txt')
for i in range(0,len(f_dof)):
    str_dof=f_dof[i].split(' ',-1)
    with open(i_path, 'a') as f:
        line='query_0711/'+str_dof[0]+'.jpg '+str_dof[1]+' '+str_dof[2]+'\n'
        f.write(line)



# f=open("/media/autolab/disk_3T/caiyingfeng/6DOF/0711/image_name/hw_val.txt")#时间戳位姿
# f_dof=list(f)
# f.close

# q_path=Path('/media/autolab/disk_3T/caiyingfeng/6DOF/0711/image_name',f'val_q.txt')
# for i in range(0,len(f_dof),5):
             
#     with open(q_path, 'a') as f:
#         line=f_dof[i]      

#         f.write(line)




# f=open("/media/autolab/disk_3T/caiyingfeng/6DOF/0808/train_data/train_db.txt")#时间戳位姿
# f_dof=list(f)
# f.close


# db_path=Path('/media/autolab/disk_3T/caiyingfeng/6DOF/0711/image_name',f'val_db.txt')
# for i in range(0,len(f_dof)):
#     if i%5==0:
#         continue

#     with open(db_path, 'a') as f:
#         line=f_dof[i]      

#         f.write(line)
#         # print(line)

# str_file=['train_db','train_q','test_db','test_q','val_db','val_q']
# str_file=['train_30k_db','train_30k_q','test_30k_db','test_30k_q','val_30k_db','val_30k_q']
# for s in str_file:

#     f=open("/media/autolab/disk_3T/caiyingfeng/6DOF/0808/train_data/"+s+".txt")#时间戳位姿
#     f_dof=list(f)
#     f.close


#     db_path=Path("/media/autolab/disk_3T/caiyingfeng/6DOF/0808/train_data/add/"+s+".txt")
#     for i in range(0,len(f_dof)):
#         str_dof=f_dof[i].split(' ',1)
#         name=str_dof[0].split('/',-1)

#         with open(db_path, 'a') as f:
#             line=f_dof[i]

#             line+=name[0]+'_0808/'+name[1]+".png "+str_dof[1]
            

#             f.write(line)
#             # print(line)
#         # break