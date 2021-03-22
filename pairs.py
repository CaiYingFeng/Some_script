import os
dir_path = '/media/autolab/disk_4T/cyf/hw/database/cam03'
image_name_list=os.listdir(dir_path)
image_name_list.sort()
filename='/media/autolab/disk_4T/cyf/localization/Herarchical-Localization/pairs/huawei/dbpairs.txt'
# with open(filename,'w') as f:
#     for i in range(0,len(image_name_list)):
#         if i<10:
#             for k in range(0,i+10):
    
#                 f.write(image_name_list[i]+' '+image_name_list[k]+'\n')

#         elif i>10 and i<=(len(image_name_list)-10):

#             for k in range(i-10,i+10):

#                 f.write(image_name_list[i]+' '+image_name_list[k]+'\n')

#         elif i>(len(image_name_list)-10) and i<(len(image_name_list)-1):
    
#             for k in range(i-10,len(image_name_list)):

#                 f.write(image_name_list[i]+' '+image_name_list[k]+'\n')

#         elif i==(len(image_name_list)-1):
        
#             for k in range(i-10,len(image_name_list)-1):

#                 f.write(image_name_list[i]+' '+image_name_list[k]+'\n')
#             f.write(image_name_list[i]+' '+image_name_list[i])
pairs_path='/media/autolab/disk_4T/cyf/localization/Herarchical-Localization/pairs/huawei/cov+seq.txt'
pairs_path2='/media/autolab/disk_4T/cyf/localization/Herarchical-Localization/pairs/huawei/cov_pair.txt'
f=open(pairs_path)
p=list(f)
pairs = [p.split(' ') for p in p]
f2=open(pairs_path2)
p=list(f2)
pairs2 = [p.split(' ') for p in p]
with open(str(pairs_path), 'r') as f:
    pairs3 = [p.split(' ') for p in f.read().split('\n')]
    if(pairs3[-1]==['']):
        del(pairs3[-1])
with open(str(pairs_path2), 'r') as f:
        pairs4 = [p.split(' ') for p in f.read().split('\n')]
print(1)
