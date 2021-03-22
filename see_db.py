import sqlite3
import os
from pathlib import Path
import numpy as np
from pyquaternion import Quaternion
from scipy.spatial.transform import Rotation as R
import argparse
import logging
import subprocess
import sys
import numpy as np
IS_PYTHON3 = sys.version_info[0] >= 3

def blob_to_array(blob, dtype, shape=(-1,)):
    if IS_PYTHON3:
        return np.fromstring(blob, dtype=dtype).reshape(*shape)
    else:
        return np.frombuffer(blob, dtype=dtype).reshape(*shape)

database_path='/media/autolab/disk_4T/cyf/localization/Herarchical-Localization/outputs/huawei/aslfeat/asl.db'
conn = sqlite3.connect(database_path)#db文件地址
cursor = conn.cursor()
sql = """select * from descriptors """

cursor.execute(sql)
result = cursor.fetchall()#result[i][1]表示id=i的图片的name
desc = blob_to_array(result[2][3], np.float16)


database_path='/media/autolab/disk_4T/cyf/localization/Herarchical-Localization/outputs/huawei/aslfeat/cam03_test.db'
conn = sqlite3.connect(database_path)#db文件地址
cursor = conn.cursor()
sql = """select * from descriptors """

cursor.execute(sql)
result1 = cursor.fetchall()#result[i][1]表示id=i的图片的name
desc1 = blob_to_array(result1[2][3], np.float16)

print(1)