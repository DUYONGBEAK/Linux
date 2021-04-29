#!/bin/sh

A=`date '+%Y-%m-%d_%H:%M:%S'`

python3 /home/kopo/test/image.py > /home/kopo/test/cap_$A.txt
