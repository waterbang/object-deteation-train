# https://storage.googleapis.com/tfjs-models/savedmodel/
FROM tensorflow/tensorflow:latest-gpu-py3

WORKDIR /env

RUN python -m pip install --upgrade pip

RUN pip install -U setuptools
RUN pip install cython
#RUN apt install -y git && git --version

COPY ./env /env
# install protobuf
RUN apt install libprotobuf-dev protobuf-compiler golang-goprotobuf-dev -y


# install tensorflows models 
#RUN git clone https://github.com/tensorflow/models.git

WORKDIR /env/models/research/
RUN protoc object_detection/protos/*.proto --python_out=.

ENV PYTHONPATH /env/models/research:/env/models:/env/models/research/slim

# install coco API
#RUN git clone https://github.com/cocodataset/cocoapi.git
WORKDIR /env/cocoapi/PythonAPI
RUN make -f /env/cocoapi/PythonAPI/Makefile
RUN cp -r pycocotools /env/models/research/

# install object deation API
WORKDIR /env/models/research/
# 国内
#RUN python -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --default-timeout=100 . 
# 需要翻墙
RUN python -m pip install .


# 此条命令是测试看看 COCO API 有没有正确安装
#RUN python object_detection/builders/model_builder_tf2_test.py

# train model
WORKDIR /env
#pre-trained-models/ssd_resnet50_v1_fpn/checkpoint/checkpoint
#RUN python model_main_tf2.py --model_dir=model/my_ssd_resnet50_v1_fpn --pipeline_config_path=model/my_ssd_resnet50_v1_fpn/pipeline.config


