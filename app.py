from plotImages import plotImages

import matplotlib.pyplot as plt
import numpy as np
import os
import random
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.image import ImageDataGenerator

gen = ImageDataGenerator(rotation_range=10, width_shift_range=0.1, height_shift_range=0.1,
                         shear_range=0.15, zoom_range=0.1, channel_shift_range=10, horizontal_flip=True)

# * Choose random image from disk
chosen_image = random.choice(os.listdir('data/dogs-vs-cats/train/dog'))

image_path = 'data/dogs-vs-cats/train/dog/' + chosen_image

# * Expand the dimensions so that the image can use for later
image = np.expand_dims(plt.imread(image_path), 0)
# plt.imshow(image[0])

# * Take data and label data, generate batches of augument data
# aug_iter = gen.flow(image)

# * Get 10 samples from augmented data and plot the images
# aug_images = [next(aug_iter)[0].astype(np.uint8) for i in range(10)]
# plotImages(aug_images)

# * Save augmented data
aug_iter = gen.flow(image, save_to_dir='data/dogs-vs-cats/train/dog',
                    save_prefix='aug-image-', save_format='jpeg')

aug_images = [next(aug_iter)[0].astype(np.uint8) for i in range(10)]
