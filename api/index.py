from flask import Flask
from flask_cors import CORS
from flask import request
import requests

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'