
import numpy as np
import os
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from tqdm import tqdm
from pathlib import Path

base_path='/media/autolab/disk_4T/cyf/localization/out/exports/netvlad/aachen/keyframe_fc_5to1'
desc_namelist=os.listdir(base_path)
desc_pathlist=[os.path.join(base_path,npz_name) for npz_name in desc_namelist]
for i in range(len(desc_namelist)):

    des=np.ones(4096, np.float32)
    mypre={'global_descriptor':des}
    mypre['input_shape']=[1200,1920,1]
    name=desc_namelist[i]
    base_dir='/media/autolab/disk_4T/cyf/localization/out/exports/netvlad/aachen/keyframe_fc_5to1'
    Path(base_dir, Path(name).parent).mkdir(parents=True, exist_ok=True)
    np.savez(Path(base_dir, '{}'.format(name)), **mypre) 