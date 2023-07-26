#!/bin/bash

# object_detection API 환경변수 세팅
path1="/home/kth/URP/optimizing-retrospective-video-analytics/models/research/"
path2="/home/kth/URP/optimizing-retrospective-video-analytics/models/research/slim"

if [[ $PYTHONPATH != *"$path1"* ]]; then
  export PYTHONPATH=$PYTHONPATH:$path1
fi

if [[ $PYTHONPATH != *"$path2"* ]]; then
  export PYTHONPATH=$PYTHONPATH:$path2
fi

# hwang 환경변수 세팅
path3="/home/kth/URP/optimizing-retrospective-video-analytics/hwang/build"

if [[ $LD_LIBRARY_PATH != *"$path3"* ]]; then
  export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$path3
fi
# run boggart app
python ./boggart-master/main.py