import faiss
import numpy as np
import os
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from tqdm import tqdm
from pathlib import Path




dbgt_path='/media/autolab/disk_3T/caiyingfeng/huawei/0808/B1/gt/front_center_5to1.txt'#database的gt
dbgt_list=list(open(dbgt_path))

querygt_path='/media/autolab/disk_4T/cyf/localization/out/eval/aachen/0711_front_center20to1.txt'
querygt_list=list(open(querygt_path))

db_path='/media/autolab/disk_4T/cyf/localization/out/exports/netvlad/aachen/db_front_center_5to1_1frame'#database的全局特征目录
db_namelist=os.listdir(db_path)
dbdes_pathlist=[os.path.join(db_path,npz_name) for npz_name in db_namelist]
db_descriptors=[]
for path in dbdes_pathlist:
    with np.load(path) as p:
        pred = {k: v.copy() for k, v in p.items()}
    db_descriptors.append(pred['global_descriptor'])
db_descriptors=np.array(db_descriptors)

query_path='/media/autolab/disk_4T/cyf/localization/out/exports/netvlad/aachen/query'
query_namelist=os.listdir(query_path)
querydes_pathlist=[os.path.join(query_path,npz_name) for npz_name in query_namelist]
query_descriptors=[]
for path in querydes_pathlist:
    with np.load(path) as p:
        pred = {k: v.copy() for k, v in p.items()}
    query_descriptors.append(pred['global_descriptor'])
query_descriptors=np.array(query_descriptors)  


faiss_index = faiss.IndexFlatL2(4096)
faiss_index.add(db_descriptors)

n_values = 1

_, predictions = faiss_index.search(query_descriptors, n_values)

estimate=[]
gt=[]
for i in range(len(predictions)):
    estimate.append([float(dbgt_list[predictions[i][0]].split()[1]), float(dbgt_list[predictions[i][0]].split()[2])])
    gt.append([float(querygt_list[i].split()[1]), float(querygt_list[i].split()[2])])
gt_x=[]
gt_y=[]
est_x=[]
est_y=[]
for i in range(len(gt)):
    gt_x.append(gt[i][0])
    gt_y.append(gt[i][1])
    est_x.append(estimate[i][0])
    est_y.append(estimate[i][1])
plt.plot(gt_x, gt_y, c='g', label="ground truth")
plt.plot(est_x, est_y, c='r', label="estimate")
# plt.scatter(gt_x, gt_y, c='g', label="ground truth")
# plt.scatter(est_x, est_y, c='r', label="estimate")

plt.legend()
plt.show()


print(1)