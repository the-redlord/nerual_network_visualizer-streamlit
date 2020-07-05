
import json
import tensorflow as tf
import numpy as np
import random

from flask import Flask, request

app = Flask(__name__)

# routes

@app.route('/')
def index():
  return 'Welcome to Model server'

if __name__ == '__main__':
  app.run()