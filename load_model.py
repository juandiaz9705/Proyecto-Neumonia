import tensorflow as tf
from tensorflow.keras import models

def model():
    try:
        model_cnn = tf.keras.models.load_model('C:/UAO/UAO-Neumonia/WilhemNet_86.h5')
        return model_cnn
    except OSError as e:
        print(f"Error loading model: {e}")
        return None
