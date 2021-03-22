# usage:terminal1:source /opt/ros/kinetic/setup.bash roscore
# terminal2:source /opt/ros/kinetic/setup.bash bag2image.py
import sys, time, argparse, re
import os
# numpy and scipy
import numpy as np

# OpenCV
import cv2

# Ros libraries
import roslib
import rospy
import rosbag

# Ros Messages
from sensor_msgs.msg import CompressedImage
import sensor_msgs.msg as sensor_msgs
import std_msgs.msg as std_msgs
cams=['front_left','front_right']
# cam='front_center'
for cam in cams:
    for i in range(0,7):
        # opts = argparse.ArgumentParser("This script is used to extract basler images from a rosbag.")
        # opts.add_argument("--input_bag", default='/media/autolab/disk_3T/caiyingfeng/huawei_parking_lot/0711/F-1/huawei-07111901_0.bag')
        # opts.add_argument("--topic", default='/camera_front_right/image_raw/compressed')
        # opts.add_argument("--output_directory", default='/media/autolab/disk_3T/caiyingfeng/im')
        # opts = opts.parse_args()
        
        input_bag='/media/autolab/disk_3T/caiyingfeng/huawei_parking_lot/0711/F-1/huawei-07111901_'+i.__str__()+'.bag'
        # input_bag='/media/autolab/disk_3T/caiyingfeng/huawei/0808/B1/2007_B1_'+i.__str__()+'.bag'
        # input_bag='/media/autolab/disk_3T/225nas/zhinengche_data/Datasets/huawei-parkinglot/huawei_parking_lot/0808/B1/2007_B1_'+i.__str__()+'.bag'
        
        # jujy
        
        if cam=='front_center':
            topic='/camera_front_center/image_raw/compressed'
        if cam=='back_left':
            topic='/camera_back_left/image_raw/compressed'
        if cam=='front_left':
            topic='/camera_front_left/image_raw/compressed'
        if cam=='back_right':
            topic='/camera_back_right/image_raw/compressed'
        if cam=='front_right':
            topic='/camera_front_right/image_raw/compressed'

        # August
        # if cam=='front_center':
        #     topic='/middlefront/compressed'
        # if cam=='back_left':
        #     topic='/leftback/compressed'
        # if cam=='front_left':
        #     topic='/leftfront/compressed'
        # if cam=='back_right':
        #     topic='/rightback/compressed'
        # if cam=='front_right':
        #     topic='/rightfront/compressed'

        # output_directory='/media/autolab/disk_3T/caiyingfeng/huawei/0808/B1/'+i.__str__()+'_'+cam+'/'
        output_directory='/media/autolab/disk_3T/caiyingfeng/huawei/0711/F1/'+cam+'/'
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)
        
        output_timestamp='/media/autolab/disk_3T/caiyingfeng/huawei/0711/F1/name_pose/'+i.__str__()+'_'+cam+'.txt'

        bag = rosbag.Bag(input_bag)
        topic_pattern = re.compile(".*"+topic+".*")

        for idx, (topic, msg, t) in enumerate(bag.read_messages()):
            # print(idx)
            if not topic_pattern.match(topic): continue
            #print "Got an image in topic:" + topic
            np_arr = np.fromstring(msg.data, np.uint8)
            img = cv2.imdecode(np_arr, 0)
            img = cv2.cvtColor(img, cv2.COLOR_BAYER_BG2BGR)
            
            outpath = "%s/%.10f.jpg" % (output_directory, t.to_sec())
            cv2.imwrite(outpath, img)

            time_stamp="%.10f"%(t.to_sec())
            # print(time_stamp)
            with open(output_timestamp,'a') as f:
                f.write(time_stamp+'\n')
            
        print(cam+" bag "+i.__str__()+' finished')


