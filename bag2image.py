
import sys, time, argparse, re

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

for i in range(0,29):
    # opts = argparse.ArgumentParser("This script is used to extract basler images from a rosbag.")
    # opts.add_argument("--input_bag", default='/media/autolab/disk_3T/caiyingfeng/huawei_parking_lot/0711/F-1/huawei-07111901_0.bag')
    # opts.add_argument("--topic", default='/camera_front_right/image_raw/compressed')
    # opts.add_argument("--output_directory", default='/media/autolab/disk_3T/caiyingfeng/im')
    # opts = opts.parse_args()
    
    #input_bag='/media/autolab/disk_3T/caiyingfeng/huawei_parking_lot/0711/F-1/huawei-07111901_'+i.__str__()+'.bag'
    input_bag='/media/autolab/disk_3T/caiyingfeng/zhinengche/Datasets/huawei-parkinglot/huawei_parking_lot/0808/B1/2007_B1_'+i.__str__()+'.bag'

    #topic='/camera_front_center/image_raw/compressed'

    #topic='/middlefront/compressed'
    # topic='/leftback/compressed'
    # topic='/leftfront/compressed'
    # topic='/rightback/compressed'
    topic='/rightfront/compressed'

    output_directory='/media/autolab/disk_3T/caiyingfeng/huawei/0808/B1/front_right/'
    #output_directory='/media/autolab/disk_3T/caiyingfeng/huawei/0711/F1/front_center/'

    bag = rosbag.Bag(input_bag)
    topic_pattern = re.compile(".*"+topic+".*")

    for idx, (topic, msg, t) in enumerate(bag.read_messages()):
        if not topic_pattern.match(topic): continue
        #print "Got an image in topic:" + topic
        np_arr = np.fromstring(msg.data, np.uint8)
        img = cv2.imdecode(np_arr, 0)
        img = cv2.cvtColor(img, cv2.COLOR_BAYER_BG2BGR)
        outpath = "%s/%.10f.jpg" % (output_directory, t.to_sec())
        cv2.imwrite(outpath, img)
    print "bag "+i.__str__()+' finish'


