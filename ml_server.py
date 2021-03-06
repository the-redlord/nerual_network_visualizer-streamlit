
import json
import tensorflow as tf
import numpy as np
import random

from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

model = tf.keras.models.load_model('model.h5')
feature_model = tf.keras.models.Model(
    model.inputs,
    [layer.output for layer in model.layers]
)

_, (x_test, _) = tf.keras.datasets.mnist.load_data()
x_test = x_test/255.

def get_preds():
  index = np.random.choice(x_test.shape[0])
  image = x_test[index,:,:]
  image_arr = np.reshape(image,(1,784))
  return feature_model.predict(image_arr), image

# routes
@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    preds, image = get_preds()
    final_preds = [p.tolist() for p in preds]
    return json.dumps({
        'prediction': final_preds,
        'image': image.tolist()
    })
  return 'Welcome to Model server'

if __name__ == '__main__':
  app.run(host='0.0.0.0')