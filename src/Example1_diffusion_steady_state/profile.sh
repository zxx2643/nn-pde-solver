#!/bin/bash

root=$PWD

batch_list=(2048 1024 512 256 128 64 32)

# loop over all the arrays
for b0 in "${batch_list[@]}" 
do
  cp octagon-32x32-cnn.ini tmp.ini
  sed -i "s/256/$b0/g" tmp.ini
  python3 main.py tmp.ini 
done
