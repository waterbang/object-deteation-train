# object-deteation-train
对象检测模型训练,此仓库已经集成了cocoAPI，Object deteationAPI等环境，让您开箱即用。

## dircetory
-   .
-   ├── Python ---> 存放xml转csv，csv转TFRcords 的python脚本
-   ├── annotations --->存放转换的TFRcords
-   ├── cocoapi ---> cocoapi
-   ├── exported-models ---> 导出的模型准备放这里
-   ├── images ---> 标记的图片train and test
        |—— train
        |—— test 
-   ├── model ---> 训练模型的目录
-   ├── models ---> tensorflow Object deteation API
-   └── pre-trained-models ---> tensorflow Object deteation model

## 开始

前置条件： labelImg 和 docker。


### 标记对象
使用[labelImg](https://github.com/tzutalin/labelImg), 标注对象，并保存xml.类似于：
![labelImg](https://xdtnyimg.waterbang.top/object-deteation.png)

### 准备映射训练集
收集完，将其放在任意目录下，训练集和测试集都放。比例自己决定。此项目提供了两种构建方法，推荐docker hub，因为它可以让您在服务器上训练，解放您的本地资源。
### 本地构建

```
git clone https://github.com/waterbang/object-deteation-train.git
```

### 创建映射容器
使用docker 构建以解决环境问题。运行：
```
docker build -t object-deteation:train .
```

### docker hub 拉取
拉镜像
```
docker pull waterbang/object-deteation
```

## 运行容器

使用本地目录映射替到容器内images目录，以便于对数据集进行操作。
>注意：以下目录对应您的训练集和测试集目录，请修改成您的。
>/Users/waterbang/Desktop/tensorflow/dog/data/images

```
docker run -it --name object-deteation -v /Users/waterbang/Desktop/tensorflow/dog/data/images:/env/images object-deteation:train bash
```
显示如下：
![tensorflow](https://xdtnyimg.waterbang.top/tensorflow-cmd.png)

## 构建并训练(如果您已经有TFRcords跳过此步)
进入 /Python 目录
### xml transform csv
先打开，`xml_to_csv.py`，修改 xml文件夹地址 和 生成csv文件地址。
记得训练集和测试集都需要转换。
在 Python 目录下运行。
``` shell
python ./xml_to_csv.py 
```

### csv transform TFRcords

1.  修改标签对应的种类数字
2.  修改文件第110行，填入数据集地址

在 Python 目录下运行.(使用绝对路径)

``` shell
python csv_to_TFRcords.py --csv_input=/env/images/train/train.csv   --output_path=/env/annotations/train.record

python csv_to_TFRcords.py --csv_input=/env/images/test/test.csv   --output_path=/env/annotations/test.record
```

### Training model

#### 先修改您的对象种类
```
vim /env/annotations/label_map.pbtxt
```

在 `model_main_tf2.py`同级目录下运行（/env）：

```
python model_main_tf2.py --model_dir=./models/ssd_resnet50_v1_fpn --pipeline_config_path=./models/ssd_resnet50_v1_fpn/pipeline.config

```

## 辅助脚本
帮您将相同大小的数据转换成xml：
`/env/node/png_to_xml.js`

批量移动文件，方便分割测试集和训练集：
`/env/node/more_test.sh`

删除一个文件夹下所有的xml文件
`/env/Python/delete_xml.py`

## 如果遇到了错误
1.  请检查脚本文件路径。

3.  使用python3。


### express heartfelt thanks

1.  https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/install.html#try-out-the-examples

2.  https://github.com/tzutalin/labelImg

3.  https://www.tensorflow.org/

4.  https://gist.github.com/olivoil/a2e0e4f3427db8b6ef4a6374f9c4cb32