import rosbag
import cv2
from cv_bridge import CvBridge
for i in range(0,7):

    bag_file = '/media/autolab/disk_3T/caiyingfeng/huawei_parking_lot/0711/F-1/huawei-07111901_'+i.__str__()+'.bag'
    bag = rosbag.Bag(bag_file, "r")
    rgb_path = '/media/autolab/disk_3T/caiyingfeng/huawei/0711/F1/front_right/' 
    bridge = CvBridge()
    bag_data = bag.read_messages('/camera_front_right/image_raw/compressed')
    for topic, msg, t in bag_data:
        #print(msg.format)
        cv_image = bridge.compressed_imgmsg_to_cv2(msg,"bgr8")
        timestr = "%.10f" %  msg.header.stamp.to_sec()
        image_name=timestr+".jpg"
        cv2.imwrite(rgb_path + image_name, cv_image)
        #cv2.imshow("Image window", cv_image)
        cv2.waitKey(3)
    

# import rosbag
# import numpy as np
# import sensor_msgs.point_cloud2 as pc2

# bag_file = 'huawei-07111901_0.bag'
# bag = rosbag.Bag(bag_file, "r")
# bag_data = bag.read_messages('/velodyne_points')

# for topic, msg, t in bag_data:
#     lidar = pc2.read_points(msg)
#     points = np.array(list(lidar))
#     print points.shape
#     # print points
#     break
# for point in points:
#    print point[0],point[1],point[2]

# import rosbag
# import sys
# from PIL import Image
# import os
# import numpy as np
# import cv2


# if __name__ == '__main__':
#     bag_dir = '/media/autolab/disk_3T/caiyingfeng' 
#     img_dir = os.path.join(bag_dir, 'image1')
#     if not os.path.exists(img_dir):
#         os.makedirs(img_dir)
#     bag_file = os.path.join(bag_dir, 'huawei-07111901_0.bag')
#     bag = rosbag.Bag(bag_file)
#     index = 0
#     imgname = os.path.join(img_dir, '{:0>5d}.jpg')
#     for topic, msg, t in bag.read_messages(topics='/camera_front_center/image_raw/compressed'):
#         header = msg.header
#         header_seq = header.seq 
#         stamp_sec = header.stamp.secs
#         stamp_nsec = header.stamp.nsecs
#         data = msg.data #bytes
#         img = np.frombuffer(data, dtype=np.uint8)
#         #img = img.reshape(1200, 1920)
#         cv2.imwrite(imgname.format(index), img)
#         print('{:0>5d} {} {} {}'.format(index, header_seq, stamp_sec, stamp_nsec))
#         index += 1
        

    # coding:utf-8
    #!/usr/bin/python
     
    # Extract images from a bag file.
     
#     #PKG = 'beginner_tutorials'
# import roslib;   #roslib.load_manifest(PKG)
# import rosbag
# import rospy
# import cv2
# from sensor_msgs.msg import Image
# from cv_bridge import CvBridge
# from cv_bridge import CvBridgeError
     
#     # Reading bag filename from command line or roslaunch parameter.
#     #import os
#     #import sys
     
# rgb_path = '/media/autolab/disk_3T/caiyingfeng/image1/'
# depth_path= '/media/autolab/disk_3T/caiyingfeng/image1/'
     
# class ImageCreator():
#     def __init__(self):
#         self.bridge = CvBridge()
#         with rosbag.Bag('huawei-07111901_0.bag', 'r') as bag:
#             for topic,msg,t in bag.read_messages():
#                 if topic == "/camera_front_left/image_raw/compressed":
#                         try:
#                             cv_image = self.bridge.compressed_imgmsg_to_cv2(msg,"bgr8")
#                         except CvBridgeError as e:
#                             print e
#                         timestr = "%.6f" %  msg.header.stamp.to_sec()

#                         image_name = timestr+ ".png"
#                         cv2.imwrite(rgb_path + image_name, cv_image) 
#                 elif topic == "camera/depth_registered/image_raw":
#                         try:
#                             cv_image = self.bridge.imgmsg_to_cv2(msg,"16UC1")
#                         except CvBridgeError as e:
#                             print e
#                         timestr = "%.6f" %  msg.header.stamp.to_sec()

#                         image_name = timestr+ ".png" 
#                         cv2.imwrite(depth_path + image_name, cv_image)
     
# if __name__ == '__main__':
#         #rospy.init_node(PKG)
#     try:
#         image_creator = ImageCreator()
#     except rospy.ROSInterruptException:
#         pass

#rosrun image_view extract_images _sec_per_frame:=0.001 image:=/camera_front_left/image_raw _image_transport:=compressed

