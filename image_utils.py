import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os
import random

gen = ImageDataGenerator(rotation_range=10, width_shift_range=0.1, height_shift_range=0.1,
                         shear_range=0.15, zoom_range=0.1, channel_shift_range=10, horizontal_flip=True)


def plot_images(images_arr):
    fig, axes = plt.subplots(1, 10, figsize=(20, 20))
    axes = axes.flatten()
    for img, ax in zip(images_arr, axes):
        ax.imshow(img)
        ax.axis('off')
    plt.tight_layout()
    plt.show()


def gen_images(chosen_image, path, num=5):
    # * Choose random image from disk
    # chosen_image = random.choice(os.listdir('data/test/healthy'))

    image_path = path + chosen_image

    # * Expand the dimensions so that the image can use for later
    image = np.expand_dims(plt.imread(image_path), 0)
    # plt.imshow(image[0])

    # * Take data and label data, generate batches of augument data
    # aug_iter = gen.flow(image)

    # * Get 10 samples from augmented data and plot the images
    # aug_images = [next(aug_iter)[0].astype(np.uint8) for i in range(10)]
    # plotImages(aug_images)

    # * Save augmented data
    aug_iter = gen.flow(image, save_to_dir=path,
                        save_prefix=chosen_image, save_format='jpg')

    aug_images = [next(aug_iter)[0].astype(np.uint8) for i in range(num)]
