from flask import Flask
from flask_cors import CORS
from flask import request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

CORS(app)

@app.route('/api/day')
def day():
    response = requests.get('https://www.seoulouba.co.kr/campaign/?cat=&qq=&q=&q1=&q2=&ar1=&ar2=&ch[]=&sort=popular')
    html_text = response.text

    # BeautifulSoup을 사용하여 HTML 텍스트 파싱
    soup = BeautifulSoup(html_text, 'html.parser')

    # 텍스트 형식으로 변환
    text_content = soup.get_text()

    return text_content


    