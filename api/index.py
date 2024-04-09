from flask import Flask
from flask_cors import CORS
from flask import request
import requests

app = Flask(__name__)

CORS(app)

@app.route('/api/day')
def day():
    response = requests.get(
        f'https://www.seoulouba.co.kr/campaign/?cat=&qq=&q=&q1=&q2=&ar1=&ar2=&ch[]=&sort=popular')

    html_text = ''.join(response.text)

    return html_text