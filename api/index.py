from flask import Flask
from flask_cors import CORS
from flask import request
import requests

app = Flask(__name__)

CORS(app)

@app.route('/api/day')
def day():

    return '??????'