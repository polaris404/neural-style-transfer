import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import tensorflow as tf
import tensorflow_hub as hub

model = hub.load('https://www.kaggle.com/models/google/arbitrary-image-stylization-v1/tensorFlow1/256/2')

def load_image(img_bytes):
    img = tf.image.decode_image(img_bytes, channels=3)
    img = tf.image.resize(img, [256, 256])
    img = tf.image.convert_image_dtype(img, tf.float32)
    img = tf.expand_dims(img/255.0, axis=0)
    return img

def generate_img(org_img, style_img):
    org_img = load_image(org_img)
    style_img = load_image(style_img)
    gen_img = model(tf.constant(org_img), tf.constant(style_img))[0]
    img_arr = (np.array(gen_img)*255).astype(np.uint8)[0]
    return img_arr