import os
str_files=['cam03','cam05','cam06','cam07','cam08']
for str_file in str_files:
    dir_path = '/media/autolab/disk_4T/cyf/hw/query/'+str_file+'/' 
    image_name_list=os.listdir(dir_path)
    image_name_list.sort()

    filename='/media/autolab/disk_4T/cyf/hw/query/'+str_file+'.txt'
    # cam03_1606405143908561706.png
    with open(filename,'w') as f:
        for i in range(0,len(image_name_list)):
            timestamp=image_name_list[i][6:16]+'.'+image_name_list[i][16:24]
            
            f.write(timestamp+'\n')