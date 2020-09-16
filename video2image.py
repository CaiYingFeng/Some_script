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
            cv2.imwrite(os.path.join(o_video, str(count).rjust(8,'0') + expand_name), frame)

        if not ret:
            break

if __name__ == '__main__':
    input='/media/autolab/disk_3T/caiyingfeng/video_image/B1/VID_20200808_213419.mp4'
    #213419
    #213437
    #213555
    output='/media/autolab/disk_3T/caiyingfeng/video_image/image/'
    
    skip_frame=30
    process_video(input, output, skip_frame)