import os
dir_path = '/media/autolab/disk_4T/cyf/localization/Herarchical-Localization/datasets/huawei/IMAGE/images/db'
image_name_list=os.listdir(dir_path)
image_name_list.sort()
filename='/media/autolab/disk_4T/cyf/localization/Herarchical-Localization/pairs/huawei/dbpairs.txt'
with open(filename,'w') as f:
    for i in range(0,len(image_name_list)):
        if i<20:
            for k in range(0,i+20):
    
                f.write('db/'+image_name_list[i]+' db/'+image_name_list[k]+'\n')

        elif i>20 and i<=(len(image_name_list)-20):

            for k in range(i-20,i+20):

                f.write('db/'+image_name_list[i]+' db/'+image_name_list[k]+'\n')

        elif i>(len(image_name_list)-20):
    
            for k in range(i-20,len(image_name_list)):

                f.write('db/'+image_name_list[i]+' db/'+image_name_list[k]+'\n')