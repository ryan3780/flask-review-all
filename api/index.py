from flask import Flask
from flask_cors import CORS
from flask import request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

CORS(app)

@app.route('/api/seoulouba')
def day():
    response = requests.get('https://www.seoulouba.co.kr/campaign/?cat=&qq=&q=&q1=&q2=&ar1=&ar2=&ch[]=&sort=popular')
    html_text = response.text

   # BeautifulSoup를 사용하여 HTML 파싱
    soup = BeautifulSoup(html_text, 'html.parser')

    # class='campaign_content'인 요소 찾기
    tum_img_elements = soup.find_all('li','campaign_content')


    all_campaigns = []
    # href와 img src 가져오기
    for tum_img in tum_img_elements:
        a_tag = tum_img.find('a','tum_img')
        href = a_tag.get('href')
        img = tum_img.find('img').get('src')

        all_campaigns.append({href : href, thumbnail : img})

    

    return all_campaigns
    


    