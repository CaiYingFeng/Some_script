import numpy as np 
import shapely
import os
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from shapely.geometry import Polygon,MultiPoint  #多边形
def iou(l1,l2):
    # line1=[2,0,2,2,0,0,0,2]   #四边形四个点坐标的一维数组表示，[x,y,x,y....]
    line1=l1
    a=np.array(line1).reshape(4, 2)   #四边形二维坐标表示
    poly1 = Polygon(a).convex_hull  #python四边形对象，会自动计算四个点，最后四个点顺序为：左上 左下  右下 右上 左上
    # print(Polygon(a).convex_hull)  #可以打印看看是不是这样子
    
    # line2=[1,1,4,1,4,4,1,4]
    line2=l2
    b=np.array(line2).reshape(4, 2)
    poly2 = Polygon(b).convex_hull
    # print(Polygon(b).convex_hull)
    
    union_poly = np.concatenate((a,b))   #合并两个box坐标，变为8*2
    #print(union_poly)
    # print(MultiPoint(union_poly).convex_hull)      #包含两四边形最小的多边形点
    if not poly1.intersects(poly2): #如果两四边形不相交
        iou = 0
    else:
        try:
            inter_area = poly1.intersection(poly2).area   #相交面积
            # print(inter_area)
            #union_area = poly1.area + poly2.area - inter_area
            union_area = MultiPoint(union_poly).convex_hull.area
            # print(union_area)
            if union_area == 0:
                iou= 0
            #iou = float(inter_area) / (union_area-inter_area)  #错了
            iou=float(inter_area) / union_area
            # iou=float(inter_area) /(poly1.area+poly2.area-inter_area)
            # 源码中给出了两种IOU计算方式，第一种计算的是: 交集部分/包含两个四边形最小多边形的面积  
            # 第二种： 交集 / 并集（常见矩形框IOU计算方式） 
        except shapely.geos.TopologicalError:
            print('shapely.geos.TopologicalError occured, iou set to 0')
            iou = 0
    
    # print(a)
    
    # print(iou)
    return iou
def str2float(strlist):
    floatlist=[]
    strlist=strlist.split(',',-1)
    for i in range(8):
        floatlist.append(float(strlist[i]))
    return floatlist


pre_dir_path = '/media/autolab/disk_4T/cyf/EAST/train/90901/txt'#预测txt的路径，我们的
pretxt_list=os.listdir(pre_dir_path)
pretxt_list.sort()

pre_dir_path_author = '/media/autolab/disk_4T/cyf/EAST/train/49491/txt'#预测txt的路径，作者
pretxt_list_author=os.listdir(pre_dir_path_author)
pretxt_list_author.sort()

gt_dir_path='/media/autolab/disk_4T/cyf/EAST/train/Challenge4_Test_Task1_GT'#真值的txt路径
tp=0
gt_box_num=0
pre_box_num=0

x_data=[]
y_data=[]
y_data_author=[]
Threshold=0
while Threshold <1:
    x_data.append(Threshold)

    for txt in pretxt_list:

        p=open(pre_dir_path+'/'+txt)#pre
        pre=list(p)
        g=open(gt_dir_path+'/gt_'+txt)#gt
        gt=list(g)
        pre_box_num+=len(pre)
        gt_box_num+=len(gt)
        for i in range(len(pre)):
            for j in range(len(gt)):
                myiou=iou(str2float(pre[i]),str2float(gt[j]))
                if(myiou>Threshold):###iou的阈值
                    tp+=1
                    

    fp=gt_box_num-tp
    fn=pre_box_num-tp
    recall=tp/(tp+fn)
    pre=tp/(tp+fp)
    f1_score=(2*pre*recall)/(pre+recall)
    y_data.append(f1_score)
    Threshold+=0.02

# print('tp='+tp.__str__())
# print('gt_box_num='+gt_box_num.__str__())
# print('pre_box_num='+pre_box_num.__str__())
# print('fp='+fp.__str__())
# print('fn='+fn.__str__())
# print('recall='+recall.__str__())
# print('pre='+pre.__str__())
# print('f1_score='+f1_score.__str__())

tp=0
gt_box_num=0
pre_box_num=0
Threshold=0
while Threshold <1:

    for txt in pretxt_list_author:

        p=open(pre_dir_path_author+'/'+txt)#pre
        pre=list(p)
        g=open(gt_dir_path+'/gt_'+txt)#gt
        gt=list(g)
        pre_box_num+=len(pre)
        gt_box_num+=len(gt)
        for i in range(len(pre)):
            for j in range(len(gt)):
                myiou=iou(str2float(pre[i]),str2float(gt[j]))
                if(myiou>Threshold):###iou的阈值
                    tp+=1
                    

    fp=gt_box_num-tp
    fn=pre_box_num-tp
    recall=tp/(tp+fn)
    pre=tp/(tp+fp)
    f1_score=(2*pre*recall)/(pre+recall)
    y_data_author.append(f1_score)
    # Threshold+=0.02


ln1,= plt.plot(x_data,y_data,color='red',linewidth=3.0,linestyle='--',label='ours')
ln2,= plt.plot(x_data,y_data_author,color='blue',linewidth=2.0,linestyle='-.',label='author’s')
# plt.plot(x_data,y_data)

plt.xlabel("IOU_Threshold")#x轴上的名字
plt.ylabel("F1_SCORE")#y轴上的名字

plt.legend(loc = 'upper right')
plt.show()
# print('tp='+tp.__str__())
# print('gt_box_num='+gt_box_num.__str__())
# print('pre_box_num='+pre_box_num.__str__())
# print('fp='+fp.__str__())
# print('fn='+fn.__str__())
# print('recall='+recall.__str__())
# print('pre='+pre.__str__())
# print('f1_score='+f1_score.__str__())

