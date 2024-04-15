from flask import Flask
from flask_cors import CORS
from flask import request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

CORS(app,origins="*")

@app.route('/api/seoulouba')
def day():
    response = requests.get('https://www.seoulouba.co.kr/campaign/?cat=&qq=&q=&q1=&q2=&ar1=&ar2=&ch[]=&sort=popular')
   

    html_text = response.text

   # BeautifulSoup를 사용하여 HTML 파싱
    soup = BeautifulSoup(html_text, 'html.parser')

    # class='campaign_content'인 요소 찾기
    campaign_contents = soup.find_all('li','campaign_content')


    all_campaigns = []

    for campaign in campaign_contents:
        a_tag = campaign.find('a','tum_img')
        href = a_tag.get('href')
        img = campaign.find('img')
        src = img.get('src')

        href_and_src = {}
        href_and_src['href'] = href
        href_and_src['src'] = src

        all_campaigns.append(href_and_src)

    

    return all_campaigns
    


    