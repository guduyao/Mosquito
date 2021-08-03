from PIL import Image
import os
from nets.yolo3 import yolo_body
from yolo import YOLO
path = []
import tensorflow as tf
os.environ["CUDA_VISIBLE_DEVICES"] = '0'   #指定第一块GPU可用
config = tf.ConfigProto()
config.gpu_options.per_process_gpu_memory_fraction = 0.5  # 程序最多只能占用指定gpu50%的显存
config.gpu_options.allow_growth = True      #程序按需申请内存
sess = tf.Session(config=config)
def file_name_find(file_dir):
    for root,dirs,files in os.walk(file_dir):
        for j in files:
            path.append(str(root)+"/"+str(j))




yolo = YOLO()
file_name_find("pic")
for i in range (0,len(path)):
    img = str(path[i])
    image = Image.open(img)
    r_image = yolo.detect_image(image)
    r_image.show()
yolo.close_session()