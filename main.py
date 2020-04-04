import tensorflow as tf
import pathlib
import numpy as np

AUTOTUNE = tf.data.experimental.AUTOTUNE


data_dir = tf.keras.utils.get_file(
  origin='https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz',
  fname='flower_photos',
  untar=True
)
data_dir = pathlib.Path(data_dir)
image_count = len(list(data_dir.glob('*/*.jpg')))

CLASS_NAMES = np.array([item.name for item in data_dir.glob('*') if item.name != "LICENSE.txt"])

roses = list(data_dir.glob('roses/*'))
for image_path in roses[:3]:
  print(image_path)
