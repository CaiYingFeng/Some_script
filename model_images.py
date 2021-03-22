

#***************************************************************#
# images.txt和database里面image顺序不一样时，改变images.txt使用 #
#**************************************************************#

import sqlite3
import os
from pathlib import Path
f=open('/media/autolab/disk_3T/caiyingfeng/pose_w2c.txt')#时间戳位姿
f_dof=list(f)
#print(f_dof[0])
#str_dof=f_dof[1].split(' ',-1)
#print(str_dof[1])
f.close
f=open('/media/autolab/disk_3T/caiyingfeng/darknet/0_front_left.txt')#图片名
im_name=list(f)
im_name.sort()
#print(len(im_name))
#rint(im_name[0])
#str_name=im_name[1].split('/',-1)
#print(str_name[-1])
f.close
i_path=Path('/media/autolab/disk_3T/caiyingfeng/map/0_front_left/model',f'images.txt')#要保存的model的images.txt
conn = sqlite3.connect("/media/autolab/disk_3T/caiyingfeng/map/0_front_left/0_front_left.db")#db文件地址
cursor = conn.cursor()
sql = """select * from images"""
#sql = """select name from sqlite_master where type='table' order by name"""
cursor.execute(sql)
result = cursor.fetchall()#result[i][1]表示id=i的图片的name
#print(result)
for i in range(0,len(im_name)):       
    
    for j in range(0,len(im_name)):
        
        str_name=im_name[j].split('/',-1)
        name=str_name[-1]
        name=name.strip("\n")
        # print(name)
        # print(result[0][1])
        
        if name==result[i][1]:
            # print(result[i][1])
            # print(j)
            # print(im_name[j])
            # print(f_dof[j])
            
            str_dof=f_dof[j].split(' ',-1)
            with open(i_path, 'a') as f:
                k=i+1
                line=k.__str__()+' '          
                line+=str_dof[1]+' '
                line+=str_dof[2]+' '
                line+=str_dof[3]+' '
                line+=str_dof[4]+' '
                line+=str_dof[5]+' '
                line+=str_dof[6]+' '
                line+=str_dof[7].strip("\n")+' ' 
                line+="1"+' '
                line+=name.__str__()+' '
                #print(line) 
                
                
        
                f.write(line+'\n'+'\n')
    

conn.close()