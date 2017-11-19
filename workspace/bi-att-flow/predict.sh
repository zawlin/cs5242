#!/bin/sh 
python3 -m basic.cli --len_opt --cluster --mode forward
python3 predict.py
