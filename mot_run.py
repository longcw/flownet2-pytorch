import os
from subprocess import call


data_root = '/data/MOT16/train'
ckpt_file = 'data/FlowNet2_checkpoint.pth.tar'

seq_names = sorted(os.listdir(data_root))
for seq_name in seq_names:
    call(['python', 'main.py',
          '--inference', '--model', 'FlowNet2', '--save_flow',
          '--inference_dataset', 'ImagesFromFolder',
          '--resume', ckpt_file,
          '--name', seq_name, '--inference_dataset_root', os.path.join(data_root, seq_name, 'img1')
          ])
