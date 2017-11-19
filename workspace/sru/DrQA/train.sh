#!/bin/sh
python3 prepro_nus.py
CUDA_VISIBLE_DEVICES=1 python3 train.py -e 60 -bs 128 --hidden_size 256
