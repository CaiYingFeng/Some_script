import cv2
import argparse
import os


def process_video(i_video, o_video, num):
    cap = cv2.VideoCapture(i_video)
    num_frame = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    expand_name = '.jpg'
    if not cap.isOpened():
        print("Please check the path.")
    cnt = 0
    count = 0
    while 1:
        ret, frame = cap.read()
        cnt += 1

        if cnt % num == 0:
            count += 1
            cv2.imwrite(os.path.join(o_video, str(count-1).rjust(5,'0') + expand_name), frame)

        if not ret:
            break

if __name__ == '__main__':
    # video_name=['VID_20200905_130904','VID_20200905_130924','VID_20200905_130951','VID_20200905_131022','VID_20200905_131100','VID_20200905_131118',
    #         'VID_20200905_133723','VID_20200905_133959','VID_20200905_134239','VID_20200905_134305','VID_20200905_135453','VID_20200905_135535','VID_20200905_135602','VID_20200905_135859','VID_20200905_153947','VID_20200905_154132','VID_20200905_154810']
    video_name=['VID_20200808_213555']

    for v_n in video_name:
        input='/media/autolab/disk_3T/caiyingfeng/huawei/'+v_n+'.mp4'

    
        output='/media/autolab/disk_3T/caiyingfeng/huawei/'+v_n+'/'
        if not os.path.exists(output):
            os.makedirs(output)

        skip_frame=1
        process_video(input, output, skip_frame)