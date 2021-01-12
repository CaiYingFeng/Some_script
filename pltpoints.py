import matplotlib.pyplot as plt
import time
import os
import sys
import tty
import termios
cam='cam03'
f=open('/media/autolab/disk_4T/cyf/localization/out/eval/aachen/'+cam+'/'+'cam03.txt')
gt_dof=list(f)
f.close

f=open('/media/autolab/disk_4T/cyf/localization/out/eval/aachen/'+cam+'/estimate.txt')
result_dof=list(f)
f.close


plt.ion()
ground_x = []
ground_y = []

result_x = []
result_y = []
  

def plt_points():
    global plt
    
    if len(ground_x) > 0 or len(result_x) > 0:
        plt.cla()

        plt.plot(ground_x, ground_y, c='r', label="ground truth")

        plt.plot(result_x, result_y, c='g', label="result pose")

        plt.legend()
    plt.pause(0.00001)  
    # os.system("pause") 



    
# for i in range(len(gt_dof)):
for i in range(190):

    ground_x.append(float(gt_dof[i].split(' ',-1)[1]))
    ground_y.append(float(gt_dof[i].split(' ',-1)[2]))
    result_x.append(float(result_dof[i].split(' ',-1)[1]))
    result_y.append(float(result_dof[i].split(' ',-1)[2]))

    plt_points()
plt.pause(2)
plt.close()
