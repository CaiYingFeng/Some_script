import numpy as np
import h5py
import numpy as np
from pathlib import Path
import os
# data=np.load('/media/autolab/disk_4T/cyf/localization/plot/1606405085.50662051.npz')
# global_des=np.load('/media/autolab/disk_4T/cyf/localization/plot/global_descriptor.npy')
# input_shape=np.load('/media/autolab/disk_4T/cyf/localization/plot/input_shape.npy')
# kp=np.load('/media/autolab/disk_4T/cyf/localization/plot/keypoints.npy')
# local_des=np.load('/media/autolab/disk_4T/cyf/localization/plot/local_descriptor_map.npy')
# score=np.load('/media/autolab/disk_4T/cyf/localization/plot/scores.npy')

# print()


#打开文件
def h5_2_npz(h5_path,npz_path):

    f = h5py.File(h5_path,'r')
    db_prefix='query'
    names = []
    f.visititems(
        lambda _, obj: names.append(obj.parent.name.strip('/'))
        if isinstance(obj, h5py.Dataset) else None)
    names = list(set(names))
    db_names = [n for n in names if n.startswith(db_prefix)]
    base_dir=npz_path
    k=0
    for i in db_names:
        k=k+1
        des=f[i]['global_descriptor'].__array__()
        mypre={'global_descriptor':des}
        mypre['input_shape']=[600,960,1]
        name=i.split('/',-1)[-1][:-4]

        Path(base_dir, Path(name).parent).mkdir(parents=True, exist_ok=True)
        np.savez(Path(base_dir, '{}.npz'.format(name)), **mypre) 

        if k % 50 == 0 :
            print("==> Batch ({}/{})".format(k,len(db_names)), flush=True)
            print(i)

def npz_2_h5(npz_path,h5_path):
    npzfiles=['db','query']
    npz_list=[]
    for strfile in npzfiles:

        dir_path = npz_path+'/'+strfile

        test_list=os.listdir(dir_path)

        for i in range(len(test_list)):
            test_list[i]=strfile+'/'+test_list[i]

        npz_list+=test_list
    
    feature_file = h5py.File(h5_path,'a')#生成h5所需

    for npz in npz_list:
        predictions=np.load(npz_path+'/'+npz)
        name=npz.strip('npz')+'png'

        grp=feature_file.create_group(name)
        grp.create_dataset('global_descriptor',data=predictions['global_descriptor'])
        grp.create_dataset('input_shape',data=predictions['input_shape'])
        # break

    feature_file.close()


if __name__ == "__main__":

    h5_path='/media/autolab/disk_4T/cyf/localization/out/exports/netvlad/aachen/cam03_db_query.h5'
    npz_path='/media/autolab/disk_4T/cyf/localization/out/exports/netvlad/aachen/db_query'
    # h5_2_npz(h5_path,npz_path)
    npz_2_h5(npz_path,h5_path)
    # global_des=np.load('/media/autolab/disk_4T/cyf/SG_PR/eva/00_DL_db.npy')
    # print("1")