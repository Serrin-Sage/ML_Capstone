# -*- coding: utf-8 -*-
"""appML.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11rdlE6r4xLlSZ3nvF8hwJ66IW1sACeNz
"""

import numpy as np
from flask import Flask, request, jsonify, render_template, send_from_directory
#from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app)
WRml = pickle.load(open("w2r.pkl","rb"))


@app.route('/recommend', methods=['GET'])
def predict():
  chicken = WRml
  #print(chicken)
  return jsonify(chicken)
  #'The next books you should read are:{}'.format(chicken)
  #return render_template('MLpage.js')
'''
@app.route('/predict', methods=['POST'])
def predict():
  beet = request.form.values()
  print(beet)
  chicken = WRml.predict(beet)
  return render_template('MLpage.js', reading_list='The next books you should read are:{}'.format(chicken))
'''

if __name__=="__main__":
  app.run(debug=True)