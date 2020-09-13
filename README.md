# object-deteation-train
对象检测模型训练

## dircetory
-   .
-   ├── Python ---> 存放xml转csv，csv转TFRcords 的python脚本
-   ├── annotations --->存放转换的TFRcords
-   ├── cocoapi ---> cocoapi
-   ├── exported-models ---> 导出的模型准备放这里
-   ├── images ---> 标记的图片 train and test
-   ├── model ---> 训练模型的目录
-   ├── models ---> tensorflow Object deteation API
-   └── pre-trained-models ---> tensorflow Object deteation model

## How to use
使用docker 构建以解决环境问题。运行：
```
docker build -t object-deteation:train .
```
使用数据卷替换容器images目录，以便于对数据集进行操作。

### Collect the graphics you want
收集完，将其放在images的目录下，训练集和测试集都放。

### Annotated image object
使用[labelImg](https://github.com/tzutalin/labelImg), 标注对象，并保存xml
![labelImg]()

文件到目录下。（数据尽量多一点，这步最麻烦）。

### xml transform csv

在 Python 目录下运行, 记得打开此文件，修改文件目录
``` shell
python ./xml_to_csv.py 
```

### csv transform TFRcords
在 Python 目录下运行.(建议使用绝对路径)

``` shell
python csv_to_TFRcords.py --csv_input=/Users/waterbang/Desktop/tensorflow/dog/images/train/zebraCrossing/train_zebraCrossing.csv   --output_path=/Users/waterbang/Desktop/tensorflow/dog/annotations/test.record
```

### Training model
在 `model_main_tf2.py`同级目录下运行：

```
python model_main_tf2.py --model_dir=./models/ssd_resnet50_v1_fpn --pipeline_config_path=./models/ssd_resnet50_v1_fpn/pipeline.config

```

## If you encounter an error
1.  请检查脚本文件路径。

2.  使用dockerfile构建，能解决环境问题（都帮你安排好了）。

3.  使用python3。


### express heartfelt thanks

1.  https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/install.html#try-out-the-examples

2.  https://github.com/tzutalin/labelImg

3.  https://www.tensorflow.org/

4.  https://gist.github.com/olivoil/a2e0e4f3427db8b6ef4a6374f9c4cb32