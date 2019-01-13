#!/usr/bin/env bash

python main.py --inference --model FlowNet2 --save_flow --inference_dataset ImagesFromFolder \
--name MOT16-05 --inference_dataset_root /data/MOT16/train/MOT16-05/img1 --resume data/FlowNet2_checkpoint.pth.tar