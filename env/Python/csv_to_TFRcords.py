'''
  使用:
  # csv_input为输入的csv文件目录，output_path为输出的文件目录
  python csv2record.py --csv_input=data/train.csv --output_path=data/train.record

  需要修改两个位置（标记为修改处）：
  #1. 'images/train'为图片所在目录
  path = os.path.join(os.getcwd(), 'images/train')
  #2. 对应的标签返回一个整数，后面需要使用
  def class_text_to_int(row_label):
    if row_label == 'floors':
        return 1
    elif row_label == 'toutu':
        return 2
    else:
        None
'''
import io
import os
from collections import OrderedDict, namedtuple

import pandas as pd
import tensorflow as tf
import tensorflow.compat.v1 as tf
from object_detection.utils import dataset_util
from PIL import Image

# from absl import flags

# FLAGS = flags.FLAGS


# 切换到脚本所在目录
# py_dir = '/'

# print(os.getcwd())
# os.chdir(py_dir)
# print(os.getcwd())

flags = tf.app.flags
flags.DEFINE_string('csv_input', '', 'Path to the CSV input')
flags.DEFINE_string('output_path', '', 'Path to output TFRecord')
FLAGS = flags.FLAGS

# 修改处：标签数字对应
def class_text_to_int(row_label):
    if row_label == 'car':
        return 1
    elif row_label == 'person':
    	return 2
    elif row_label == 'red light':
    	return 3
    elif row_label == 'green light':
    	return 4
    else:
        return 0

'''
csv按照图片名分组；
将同一图片名中多个标记区域分为一组；
'''
def split(df, group):
    data = namedtuple('data', ['filename', 'object']) # data有两个属性，filename和object
    gb = df.groupby(group) # 按照'filename'对data中的数据进行分组
    # data(filename, gb.get_group(x))存放每个图片名、该图片的相关信息
    return [data(filename, gb.get_group(x)) for filename, x in zip(gb.groups.keys(), gb.groups)]

def create_tf_example(group, path):
    with tf.gfile.GFile(os.path.join(path, '{}'.format(group.filename)), 'rb') as fid: # rb指定二进制形式读取图片
        encoded_jpg = fid.read()
    encoded_jpg_io = io.BytesIO(encoded_jpg)
    image = Image.open(encoded_jpg_io)
    width, height = image.size

    filename = group.filename.encode('utf8')
    image_format = b'jpg'
    xmins = []
    xmaxs = []
    ymins = []
    ymaxs = []
    classes_text = []
    classes = []

    for index, row in group.object.iterrows():
        xmins.append(row['xmin'] / width)
        xmaxs.append(row['xmax'] / width)
        ymins.append(row['ymin'] / height)
        ymaxs.append(row['ymax'] / height)
        classes_text.append(row['class'].encode('utf8'))
        classes.append(class_text_to_int(row['class']))

    tf_example = tf.train.Example(features=tf.train.Features(feature={
        'image/height': dataset_util.int64_feature(height),
        'image/width': dataset_util.int64_feature(width),
        'image/filename': dataset_util.bytes_feature(filename),
        'image/source_id': dataset_util.bytes_feature(filename),
        'image/encoded': dataset_util.bytes_feature(encoded_jpg),
        'image/format': dataset_util.bytes_feature(image_format),
        'image/object/bbox/xmin': dataset_util.float_list_feature(xmins),
        'image/object/bbox/xmax': dataset_util.float_list_feature(xmaxs),
        'image/object/bbox/ymin': dataset_util.float_list_feature(ymins),
        'image/object/bbox/ymax': dataset_util.float_list_feature(ymaxs),
        'image/object/class/text': dataset_util.bytes_list_feature(classes_text),
        'image/object/class/label': dataset_util.int64_list_feature(classes),
    }))
    return tf_example

def main(_):
    writer = tf.io.TFRecordWriter(FLAGS.output_path)
    path = os.path.join(os.getcwd(), '/Users/waterbang/Desktop/tensorflow/dog/images/train/campus') # 修改处
    examples = pd.read_csv(FLAGS.csv_input)
    grouped = split(examples, 'filename')
    for group in grouped:
        tf_example = create_tf_example(group, path)
        writer.write(tf_example.SerializeToString())

    writer.close()
    output_path = os.path.join(os.getcwd(), FLAGS.output_path)
    print('Successfully created the TFRecords: {}'.format(output_path))

if __name__ == '__main__':
    tf.compat.v1.app.run()

