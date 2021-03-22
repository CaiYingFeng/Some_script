import numpy as np
import os
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from tqdm import tqdm
from pathlib import Path
import shutil
def normalize(l, axis=-1):
    return np.array(l) / np.linalg.norm(l, axis=axis, keepdims=True)

def preprocess(global_descriptors):
    global_descriptors = normalize(global_descriptors.astype(np.float32))
    transf = [lambda x: normalize(x.astype(np.float32, copy=False))]
    pca = PCA(n_components=4096, svd_solver='full')
    global_descriptors = normalize(
        pca.fit_transform(global_descriptors).astype(np.float32))
    transf.append(lambda x: normalize(
            pca.transform(x).astype(np.float32, copy=False)))

    def f(x):
        for t in transf:
            x = t(x)
        return x
    return global_descriptors,f

def check_add(new, database):
    
    dist = 2 * (1 - database @ new)#矩阵乘法
    if np.min(dist)>1.3:
        return True
    else:
        return False

def dis(p1,p2):
    d=np.sum((float(p1[0])-float(p2[0]))**2+(float(p1[1])-float(p2[1]))**2+(float(p1[2])-float(p2[2]))**2)
    d=np.sqrt(d)

    return d

plt.ion()
tra_x=[]
tra_y=[]
gt_x=[]
gt_y=[]
  

def plt_points():
    global plt
    
    if len(tra_x) > 0 or len(tra_x) > 0:
        plt.cla()

        plt.scatter(tra_x, tra_y, c='r', label="key frame")
        plt.plot(gt_x, gt_y, c='g', label="ground truth")

        plt.legend()
    plt.pause(0.000001) 

gt_path='/media/autolab/disk_3T/caiyingfeng/huawei/0808/B1/gt/front_center_5to1.txt'#database的gt
gt_list=list(open(gt_path))


base_path='/media/autolab/disk_4T/cyf/localization/out/exports/netvlad/aachen/db_front_center_5to1_1frame'#database的全局特征目录
desc_namelist=os.listdir(base_path)
desc_pathlist=[os.path.join(base_path,npz_name) for npz_name in desc_namelist]
descriptors=[]
for path in desc_pathlist:
    with np.load(path) as p:
        pred = {k: v.copy() for k, v in p.items()}
    descriptors.append(pred['global_descriptor'])
descriptors=np.array(descriptors)    
pred_desc, global_transform=preprocess(descriptors)

database=[]
database_dis=[]
database.append(pred_desc[0])
database_dis.append([float(gt_list[0].split()[1]),float(gt_list[0].split()[2]),float(gt_list[0].split()[3])])
# database=np.array(database)
count=1

for i in tqdm(range(len(pred_desc))):
    gt_x.append(float(gt_list[i].split()[1]))
    gt_y.append(float(gt_list[i].split()[2]))
    des_flag=False
    #先根据描述子判断是否加入，若加入则不需要再进行距离判断，若没加入，咋判断待加入帧5m内是否已经有帧，若无则加入
    if check_add(pred_desc[i], database):
        des_flag=True
        count+=1
        shutil.copy(desc_pathlist[i], base_path+'/'+desc_namelist[i])
        database.append(pred_desc[i])
        database_dis.append([float(gt_list[i].split()[1]),float(gt_list[i].split()[2]),float(gt_list[i].split()[3])])
        tra_x.append(float(gt_list[i].split()[1]))
        tra_y.append(float(gt_list[i].split()[2]))
        
        # continue
        # print(i)
        # database=np.array(database)
    
    dis_flag=True
    for j in range(len(database_dis)):
        if dis(database_dis[j],[float(gt_list[i].split()[1]),float(gt_list[i].split()[2]),float(gt_list[i].split()[3])])<5:
            dis_flag=False#已经有一个小于5m的帧了，不需要加入
            break
    if dis_flag:
        count+=1
        shutil.copy(desc_pathlist[i], base_path+'/'+desc_namelist[i])
        database_dis.append([float(gt_list[i].split()[1]),float(gt_list[i].split()[2]),float(gt_list[i].split()[3])])
        database.append(pred_desc[i])
        tra_x.append(float(gt_list[i].split()[1]))
        tra_y.append(float(gt_list[i].split()[2]))
        
        
    # if not dis_flag and not des_flag:
    #     des=np.ones(4096, np.float32)
    #     mypre={'global_descriptor':des}
    #     mypre['input_shape']=[1200,1920,1]
    #     name=desc_namelist[i]
    #     base_dir='/media/autolab/disk_4T/cyf/localization/out/exports/netvlad/aachen/keyframe_fc_5to1'
    #     Path(base_dir, Path(name).parent).mkdir(parents=True, exist_ok=True)
    #     np.savez(Path(base_dir, '{}'.format(name)), **mypre) 
        
    
    plt_points()
plt.pause(100)
plt.close()
print(count)


# base_path1='/media/autolab/disk_4T/cyf/localization/out/exports/netvlad/aachen/db_front_center_5to1_1frame'#database的全局特征目录
# desc_namelist1=os.listdir(base_path1)
# desc_pathlist1=[os.path.join(base_path1,npz_name) for npz_name in desc_namelist1]

# base_path2='/media/autolab/disk_4T/cyf/localization/out/exports/netvlad/aachen/keyframe_fc_5to1'#database的全局特征目录
# desc_namelist2=os.listdir(base_path2)
# desc_pathlist2=[os.path.join(base_path2,npz_name) for npz_name in desc_namelist2]
# base_path3='/media/autolab/disk_4T/cyf/localization/out/exports/netvlad/aachen/keyframe'
# for i in desc_namelist1:
#     if i not in desc_namelist2:
#         shutil.copy(base_path1+'/'+i, base_path3+'/'+i)