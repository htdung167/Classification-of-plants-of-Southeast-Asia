# from matplotlib.pyplot import axis
# from sympy import hyper
import hyper as hp
import tensorflow as tf
import numpy as np
import os
import json
# import cv2 as cv
from tensorflow.keras.preprocessing.image import img_to_array


# Load model
def _load_model():
    # os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
    # abpath = os.path.abspath(".")
    try:
        model_path = os.path.join("./flask_api/saved_models", hp.MODEL_NAME)
        with tf.device('/cpu:0'):
            model = tf.keras.models.load_model(model_path)     
    except:
        model_path = os.path.join("./saved_models", hp.MODEL_NAME)
        with tf.device('/cpu:0'):
            model = tf.keras.models.load_model(model_path)
    return model
    # print(model_path)
    

# Pre process image
def _preprocess_image(img, shape):
    img = img.resize(shape)
    img = img_to_array(img)
    img = img / 255.0
    img = np.expand_dims(img, axis=0)
    return img

# Encoding numpy to json
class NumpyEncoder(json.JSONEncoder):
    '''
    Encoding numpy into json
    '''
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        if isinstance(obj, np.int32):
            return int(obj)
        if isinstance(obj, np.int64):
            return int(obj)
        if isinstance(obj, np.float32):
            return float(obj)
        if isinstance(obj, np.float64):
            return float(obj)
        return json.JSONEncoder.default(self, obj)

