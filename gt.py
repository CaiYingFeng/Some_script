import os
dir_path = '/media/autolab/disk_4T/cyf/EAST/gt'#gttxt的路径
out_path = '/media/autolab/disk_4T/cyf/EAST/gt_out'#out gt txt的路径
txt_list=os.listdir(dir_path)
txt_list.sort()
for txt in txt_list:
    g=open(dir_path+'/'+txt)#gt
    gt=list(g)
    for i in range(len(gt)):
        with open(out_path+'/'+txt, 'a') as f:
            gt_list=gt[i].split(',')
            line=''
            for j in range(7):
                line+=gt_list[j]+','
            line+=gt_list[7]    
            f.write(line+'\n')
