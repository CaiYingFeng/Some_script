import sqlite3
import os
import sys
import numpy as np
IS_PYTHON3 = sys.version_info[0] >= 3
def array_to_blob(array):
    if IS_PYTHON3:
        return array.tostring()
    else:
        return np.getbuffer(array)
def blob_to_array(blob, dtype, shape=(-1,)):
    if IS_PYTHON3:
        return np.fromstring(blob, dtype=dtype).reshape(*shape)
    else:
        return np.frombuffer(blob, dtype=dtype).reshape(*shape)
# f = open("/media/autolab/disk_4T/cyf/map/model/images.txt","r")#id,qw,qx,qy,qz,tx,ty,tz,cid,name
# dof=list(f)
# f.close
# f_dof=list()
# for i in range(0,len(dof),2):
#     f_dof.append(dof[i])

# print(len(f_dof))
conn = sqlite3.connect("/media/autolab/disk_4T/cyf/map/3to1.db")#db文件地址
cursor = conn.cursor()

# sql = """select * from images"""
# cursor.execute(sql)
# result = cursor.fetchall()#result[i][1]表示id=i的图片的name

# print(len(result))
for i in range(0,len(result)):#len(result)
    #print(i)
    str_dof=f_dof[i].split(' ',-1)
    str_name=str_dof[9].strip('\n')
    myqw=float(str_dof[1])
    myqx=float(str_dof[2])
    myqy=float(str_dof[3])
    myqz=float(str_dof[4])
    mytx=float(str_dof[5])
    myty=float(str_dof[6])
    mytz=float(str_dof[7])
    # print(str_name)
    # print(myqw,mytz)

    cursor.execute(
            "update images set prior_qw=?,prior_qx=?,prior_qy=?,prior_qz=?,prior_tx=?,prior_ty=?,prior_tz=? where name=?",
            (myqw,myqx,myqy,myqz,mytx,myty,mytz,str_name))
    
    conn.commit()  #提交，以保存执行结果

#更新表cameras
cursor.execute('SELECT params FROM cameras WHERE camera_id=?;',
                (1,))
data = cursor.fetchall()
intrinsics = blob_to_array(data[0][0], np.double)

intrinsics[0]=1938.34
intrinsics[1]=1937.10
intrinsics[2]=959.5
intrinsics[3]=509.5


cursor.execute('UPDATE cameras SET params = ?;',
                [array_to_blob(intrinsics)])

    
conn.commit()  #提交，以保存执行结果

conn.close()

