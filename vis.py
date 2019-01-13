import os
import cv2
import numpy as np
import argparse

from utils.flow_utils import readFlow, plot_flow


parser = argparse.ArgumentParser()
parser.add_argument('-p', '--path', type=str, required=True)
parser.add_argument('-ip', '--image-path', type=str, default='')


args = parser.parse_args()

flow_root = args.path
image_root = args.image_path
flow_names = sorted(os.listdir(flow_root))
image_names = sorted(os.listdir(image_root)) if image_root else None

wait_time = 10
for i, flow_name in enumerate(flow_names):
    flow_file = os.path.join(flow_root, flow_name)
    flow = readFlow(flow_file)
    flow2show = plot_flow(flow)
    cv2.imshow('flow', flow2show)

    if image_names is not None:
        image1 = cv2.imread(os.path.join(image_root, image_names[i]))
        image2 = cv2.imread(os.path.join(image_root, image_names[i+1]))
        image2show = np.hstack((image1, image2))
        cv2.imshow('image', image2show)

    key = chr(cv2.waitKey(wait_time) % 128)
    if key == 'a':
        wait_time = 0 if wait_time else 10
        cv2.waitKey(0)
    elif key == 'q':
        break


