from flask import Flask
from flask_cors import CORS
from flask import request
import requests

app = Flask(__name__)

CORS(app)

@app.route('/api/day')
def day():

    headers = {
    }

    response = requests.get(
        f'https://api.weble.net/v1/campaigns?cat=%EC%A7%80%EC%97%AD&limit=35&media%5B%5D=blog&media%5B%5D=instagram&media%5B%5D=youtube&page=1&sort=latest&type=play', headers=headers)

    print(response)
    return response