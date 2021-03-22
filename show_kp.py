from PIL import Image
from pylab import imshow
from pylab import array
from pylab import plot
from pylab import title
import numpy as np
# 读取图像到数组中
im = array(Image.open("/media/autolab/disk_4T/cyf/localization/plot/1606405085.50662051.png"))
# 绘制图像
imshow(im)
# 一些点
kp=np.load('/media/autolab/disk_4T/cyf/localization/plot/keypoints.npy')
x=[]
y=[]
print(len(kp))
for i in range(len(kp)):
    x.append(kp[i][0])
    y.append(kp[i][1])
# 使用红色星状标记绘制点
plot(x,y,'r.')
# 绘制连接前两个点的线
#plot(x[:2],y[:2])
# 添加标题，显示绘制的图像
title('Plotting: "empire.jpg"')
# im.show()