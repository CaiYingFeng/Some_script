import os
from pyquaternion import Quaternion
from scipy.spatial.transform import Rotation as R
import numpy as np
# #querylist
# dir_path = "/media/autolab/disk_3T/caiyingfeng/huawei/mobile_query"#query_image目录。要改
# image_name_list=os.listdir(dir_path)
# image_name_list.sort()
# filename="/media/autolab/disk_4T/cyf/localization/data/aachen/mobile_query.txt"#querylist。要改
# with open(filename,'w') as f:
#     for i in range(0,len(image_name_list)):
        ##0711##
        # f.write('query/'+image_name_list[i]+' PINHOLE 1920 1200 1072.613144 1072.495216 933.757082 579.491254\n')#front_left
        # f.write('query/'+image_name_list[i]+' PINHOLE 1920 1200 1068.790865 1068.63618 971.96159 577.820583\n')#front_right
        # f.write('query/'+image_name_list[i]+' PINHOLE 1920 1200 1077.319838 1076.431366 955.747465 600.50007\n')#front_center
        ##0808##
        # f.write('query/'+image_name_list[i]+' PINHOLE 1920 1200 1073.592178 1072.747494 950.691541 585.321928\n')#front_left
        # f.write('query/'+image_name_list[i]+' PINHOLE 1920 1200 1068.790865 1068.63618 971.96159 577.820583\n')#front_right
        # f.write('query/'+image_name_list[i]+' PINHOLE 1920 1200 1077.319838 1076.431366 959.747465 600.50007\n')#front_center
        
        # f.write('query/'+image_name_list[i]+' PINHOLE 1920 1020 1938.34597 1937.09807 959.5 509.5\n')#cam03
        # f.write('query/'+image_name_list[i]+' PINHOLE 1920 1020 956.1788 957.3191 942.1158 534.9691\n')#cam05
        # f.write('query/'+image_name_list[i]+' PINHOLE 1920 1020 960.2269 961.1119 931.0223 527.5472\n')#cam06
        # f.write('query/'+image_name_list[i]+' PINHOLE 1920 1020 958.677 959.2314 944.9455 541.0408\n')#cam07
        # f.write('query/'+image_name_list[i]+' PINHOLE 1920 1020 961.4182 961.5139 933.085 538.4962\n')#cam08

        ##mobile_query##
        # f.write('query/'+image_name_list[i]+' PINHOLE 1920 1080 738.6414 1054.087 655.605 520.807\n')

        
# # #query_image gt c2w
f=open('/media/autolab/disk_3T/caiyingfeng/huawei/0711/F1/gt/fusion_v12/front_right.txt')#time tx ty tz qx qy qz qw正好是rpg所需，真值。要改
f_dof=list(f)
f.close
step=20#要改 
for i in range(0,len(f_dof),step):#根据每隔几张取图建图定步长，可能要改起点
    with open('/media/autolab/disk_4T/cyf/localization/out/eval/aachen/0711_front_right_20to1_fusion_v12_original.txt', 'a') as f:#输出的query的位姿真值c2w。要改
        f.write(f_dof[i])


# # #query_image gt c2w
# cam='0711_front_center_20to1_fusion'#query位置真值，c2w。要改
# if os.path.exists('/media/autolab/disk_4T/cyf/localization/out/eval/aachen/estimate1.txt'):
#         os.remove('/media/autolab/disk_4T/cyf/localization/out/eval/aachen/estimate1.txt')
# i_path='/media/autolab/disk_4T/cyf/localization/out/eval/aachen/estimate1.txt'
# f=open('/media/autolab/disk_4T/cyf/localization/out/eval/aachen/'+cam+'.txt')
# f_dof=list(f)
# f.close
# for i in range(0,len(f_dof)):
#     str_dof=f_dof[i].split(' ',-1)             
#     with open(i_path, 'a') as f:
#         line=str_dof[0]+' '          
                
#         line+=str_dof[7].strip("\n")+' '
#         line+=str_dof[4]+' '
#         line+=str_dof[5]+' '                            
#         line+=str_dof[6]+' '

#         line+=str_dof[1]+' '
#         line+=str_dof[2]+' '
#         line+=str_dof[3]+' '
                
#         f.write(line+'\n')

# f = open("/media/autolab/disk_4T/cyf/localization/out/eval/aachen/estimate1.txt","r")#c2w:time qw,qx,qy,qz,tx,ty,tz,单纯换了个顺序


# f_dof=list(f)
# f_dof.sort()
# f.close

# i_path='/media/autolab/disk_4T/cyf/localization/out/eval/aachen/'+cam+'_w2c.txt'#要保存w2c:name qw,qx,qy,qz,tx,ty,tz
# for i in range(0,len(f_dof)):               
#     str_dof=f_dof[i].split(' ',-1)
#     with open(i_path, 'a') as f:
#         qw = float(str_dof[1])        
#         qx = float(str_dof[2])
#         qy = float(str_dof[3])
#         qz = float(str_dof[4])
        
#         # tx = float(str_dof[5])-368516#要改
#         # ty = float(str_dof[6])-3459036
#         # tz = float(str_dof[7])-15
#         tx = float(str_dof[5])
#         ty = float(str_dof[6])
#         tz = float(str_dof[7])
#         r = R.from_quat([qx,qy,qz,qw])
#         rotation = r.as_matrix()
        
#         translation = np.asarray([tx,ty,tz])
#         xyz = -np.dot(np.linalg.inv(rotation),translation)
#         xyz = np.reshape(xyz,(1,3))

        
#         r = R.from_matrix(np.linalg.inv(rotation))
#         r2=r.as_quat()#qx,qy,qz,qw

#         line=str_dof[0]+".jpg "#time。要改

#         #qw qx qy qz
#         line+=r2[3].__str__()+' '
#         line+=r2[0].__str__()+' '
#         line+=r2[1].__str__()+' '
#         line+=r2[2].__str__()+' '

#         #tx ty tz
#         # line+=(xyz[0][0]+368516).__str__()+' '   #要改
#         # line+=(xyz[0][1]+3459036).__str__()+' '
#         # line+=(xyz[0][2]+15).__str__()
#         line+=(xyz[0][0]).__str__()+' '   
#         line+=(xyz[0][1]).__str__()+' '
#         line+=(xyz[0][2]).__str__()
#         #print(line)

#         f.write(line+'\n')
# if os.path.exists('/media/autolab/disk_4T/cyf/localization/out/eval/aachen/estimate1.txt'):
#     os.remove('/media/autolab/disk_4T/cyf/localization/out/eval/aachen/estimate1.txt')