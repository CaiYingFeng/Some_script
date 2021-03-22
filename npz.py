import os
import shutil
import numpy as np
from pathlib import Path
######
######选择npz
######
# # dir_path = "/media/autolab/disk_4T/cyf/localization/out/exports/netvlad/aachen/database/cam03/"
# dir_path = "/media/autolab/disk_4T/cyf/hw/database/cam358"#图片路径
# npz_name_list=os.listdir(dir_path)
# npz_name_list.sort()

# cam03_path = "/media/autolab/disk_4T/cyf/localization/out/exports/netvlad/aachen/database/cam03"
# cam03=os.listdir(cam03_path)
# cam03.sort()

# cam05_path = "/media/autolab/disk_4T/cyf/localization/out/exports/netvlad/aachen/database/cam05"
# cam05=os.listdir(cam05_path)
# cam05.sort()

# cam08_path = "/media/autolab/disk_4T/cyf/localization/out/exports/netvlad/aachen/database/cam08"
# cam08=os.listdir(cam08_path)
# cam08.sort()
# # f=open('/media/autolab/disk_4T/cyf/hw/database/database_timestamp/cam03.txt')
# # cam03=list(f)
# # cam03.sort()


# # f=open('/media/autolab/disk_4T/cyf/hw/database/database_timestamp/cam05.txt')
# # cam05=list(f)
# # cam05.sort()

# # f=open('/media/autolab/disk_4T/cyf/hw/database/database_timestamp/cam08.txt')
# # cam08=list(f)
# # cam08.sort()

# path='/media/autolab/disk_4T/cyf/localization/out/exports/netvlad/aachen/database/'

# for i in range(len(cam03)):
#     name=cam03[i].strip('npz')+'png'
#     if name in npz_name_list:
#         shutil.copy(cam03_path +'/'+cam03[i], path +'cam358/'+ cam03[i])

# for i in range(len(cam05)):
#     name=cam05[i].strip('npz')+'png'
#     if name in npz_name_list:
#         shutil.copy(cam05_path +'/'+ cam05[i], path +'cam358/'+ cam05[i])

# for i in range(len(cam08)):
#     name=cam08[i].strip('npz')+'png'
#     if name in npz_name_list:
#         shutil.copy(cam08_path +'/'+ cam08[i], path +'cam358/'+ cam08[i])
# # for i in range(len(npz_name_list)):

# #     npz_name=npz_name_list[i].strip('npz')+'\n'

# #     if npz_name in cam03:
# #         shutil.copy(dir_path + npz_name_list[i],path +'db_03/'+ npz_name_list[i])

#     # elif npz_name in cam05:
#     #     shutil.copy(dir_path + npz_name_list[i],path +'db_05/'+ npz_name_list[i])

#     # elif npz_name in cam08:
#     #     shutil.copy(dir_path + npz_name_list[i],path +'db_08/'+ npz_name_list[i])


# #####################
# #### 合并npz ########
# #####################


# # cam03_path = "/media/autolab/disk_4T/cyf/localization/out/exports/netvlad/aachen/database/cam03/"
# # cam03_name_list=os.listdir(cam03_path)
# # cam03_name_list.sort()
# # cam05_path = "/media/autolab/disk_4T/cyf/localization/out/exports/netvlad/aachen/database/cam05/"
# # cam05_name_list=os.listdir(cam05_path)
# # cam05_name_list.sort()
# # cam08_path = "/media/autolab/disk_4T/cyf/localization/out/exports/netvlad/aachen/database/cam08/"
# # cam08_name_list=os.listdir(cam08_path)
# # cam08_name_list.sort()

# # out_path='/media/autolab/disk_4T/cyf/localization/out/exports/netvlad/aachen/db/'
# # for i in range(len(cam03_name_list)):
# #     if i>=len(cam08_name_list):
# #         pre_03=np.load(cam03_path+'/'+cam03_name_list[i])
# #         pre_05=np.load(cam05_path+'/'+cam05_name_list[i])
# #         pre_08=np.load(cam08_path+'/'+cam08_name_list[-1])

# #     elif i<len(cam08_name_list):
# #         pre_03=np.load(cam03_path+'/'+cam03_name_list[i])
# #         pre_05=np.load(cam05_path+'/'+cam05_name_list[i])
# #         pre_08=np.load(cam08_path+'/'+cam08_name_list[i])
# #     #4096
# #     # des=pre_05['global_descriptor']+pre_03['global_descriptor']+pre_08['global_descriptor']


# #     #12288
# #     des=np.array(pre_05['global_descriptor'].tolist()+pre_03['global_descriptor'].tolist()+pre_08['global_descriptor'].tolist()).astype(np.float32)
# #     mypre={'global_descriptor':des}
# #     mypre['input_shape']=[600,960,1]

# #     name=cam03_name_list[i].strip('.npz')


# #     Path(out_path, Path(name).parent).mkdir(parents=True, exist_ok=True)
# #     np.savez(Path(out_path, '{}.npz'.format(name)), **mypre) 


# # ######测试####
# # pre=np.load(out_path+'1606405085.50662051.npz')
# # pre1=np.load(cam03_path+'1606405085.50662051.npz')
# # print("1")


# ###################
# ####用1补齐npz#####
# ###################
# # dball_path = "/media/autolab/disk_4T/cyf/localization/out/exports/netvlad/aachen/db_4096/"
# # db_all_npz=os.listdir(dball_path)
# # db_all_npz.sort()

# # db_path = "/media/autolab/disk_4T/cyf/localization/out/exports/netvlad/aachen/db_just_cam03/"
# # db_npz=os.listdir(db_path)
# # db_npz.sort()

# # out_path='/media/autolab/disk_4T/cyf/localization/out/exports/netvlad/aachen/db_1/'

# # for i in range(len(db_all_npz)):
# #     if db_all_npz[i] in db_npz:
# #         continue

# #     des=np.array([10]*4096).astype(np.float32)
# #     mypre={'global_descriptor':des}
# #     mypre['input_shape']=[600,960,1]

# #     name=db_all_npz[i].strip('.npz')


# #     Path(out_path, Path(name).parent).mkdir(parents=True, exist_ok=True)
# #     np.savez(Path(out_path, '{}.npz'.format(name)), **mypre) 
fc=list(open('/media/autolab/disk_3T/caiyingfeng/huawei/0808/B1/gt/front_center_10to1_half.txt'))
fl=list(open('/media/autolab/disk_3T/caiyingfeng/huawei/0808/B1/gt/front_left_10to1_half.txt'))
fr=list(open('/media/autolab/disk_3T/caiyingfeng/huawei/0808/B1/gt/front_right_10to1_half.txt'))
name=[]
for f in [fc,fl,fr]:
    for i in range(len(f)):
        name.append(f[i].split(' ')[0])

npz_path = "/media/autolab/disk_4T/cyf/localization/out/exports/netvlad/aachen/front_10to1"
npz=os.listdir(npz_path)
npz.sort() 
npz_path_list=[os.path.join(npz_path,npz_name)for npz_name in npz]
for i in range(len(npz)):
    if npz[i].strip('.npz') in name:
        shutil.copy(npz_path_list[i],"/media/autolab/disk_4T/cyf/localization/out/exports/netvlad/aachen/db/"+ npz[i])
