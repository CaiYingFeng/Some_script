import os
strfiles=['cam03.txt','cam05.txt','cam06.txt','cam07.txt','cam08.txt']
for strfile in strfiles:
    f=open('/media/autolab/disk_4T/cyf/hw/query/query_timestamp/'+strfile)#timestamnp
    times=list(f)
    f.close
    

    f=open('/media/autolab/disk_4T/cyf/hw/camera_pose/query/'+strfile)#dof
    dofs=list(f)
    f.close
    
    filename='/media/autolab/disk_4T/cyf/hw/query/changed/'+strfile
            
    with open(filename,'w') as f:
        for i in range(0,len(times)):
            print(i)
            f.write(times[i].strip('\n')+' '+dofs[i].split(' ',1)[1])
            # print(times[i])
            # print(dofs[i])
            # print(times[i].strip('\n')+' '+dofs[i].split(' ',1)[1]+'\n')
            # break
