from flask import Flask
from flask_cors import CORS
from flask import request
import requests

app = Flask(__name__)
CORS(app)

@app.route('/api/day')
def day():

    response = requests.get(
        f'https://www.reviewplace.co.kr/pr/?&ct1=%EC%A7%80%EC%97%AD&s_sst=popu&s_sod=desc')

    print(response)
    return response