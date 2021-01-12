import os
import json
import string


def create_json(input_txt_path,output_josn_path,pose):

    data = json.load(open('/media/autolab/disk_4T/cyf/SG_PR/data/0.json'))#给个格式，没什么用
    
    f=open(input_txt_path)#特征点位置
    s_dof=list(f)

    data['centers'].clear()
    data['nodes'].clear()
    data['pose'].clear()

    for i in range(len(s_dof)):
        
        s=s_dof[i].split(' ',-1)
        s=s[0:3]
        s[0]=float(s[0])
        s[1]=float(s[1])
        s[2]=float(s[2])
        data['centers'].append(s)
        data['nodes'].append(0)
        
        # print(s)
        # break
    
    
    pose_str=pose.split(' ',-1)
    for i in range(len(pose_str)):
        data['pose'].append(float(pose_str[i]))


    
    with open(output_josn_path,'w') as file_obj:
        json.dump(data,file_obj)

files=['01','02','03','05','06','07','08','09','10']
for file in files:
    f_pose=open('/media/autolab/disk_4T/cyf/SG_PR/SG_PR_DATA/graphs_rn/rest/poses/'+file+'.txt')#pose
    pose=list(f_pose)

    dir_path = '/media/autolab/disk_4T/cyf/SG_PR/SG_PR_DATA/graphs_rn/rest/'+file+'/keypoints'
    txt_list=os.listdir(dir_path)
    txt_list.sort()

    # print(txt_list[1])
    num=0
    for txt_name in txt_list:
        if not os.path.exists('/media/autolab/disk_4T/cyf/SG_PR/SG_PR_DATA/graphs_rn/'+file):
            os.makedirs('/media/autolab/disk_4T/cyf/SG_PR/SG_PR_DATA/graphs_rn/'+file)
        create_json(dir_path+'/'+txt_name,'/media/autolab/disk_4T/cyf/SG_PR/SG_PR_DATA/graphs_rn/'+file+'/'+txt_name.strip('.txt')+'.json',pose[num])
        num+=1




    print("finished"+file)