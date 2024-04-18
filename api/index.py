from flask import Flask
from flask_cors import CORS
from flask import request
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

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

    today = datetime.today()

    all_campaigns = []

    for campaign in campaign_contents:

        d_day = campaign.find('div', 'd_day')
        minus_day = d_day.text.replace("\r", "").replace("\n", "").replace("\t", "").replace("D-", "")

        if minus_day == '마감':
            continue
        else:
            a_tag = campaign.find('a','tum_img')
            href = a_tag.get('href')
            img = campaign.find('img')
            src = img.get('src')
            title = campaign.find('strong', 's_campaign_title')
            description = campaign.find('span', 'basic_blue')
            recruit = campaign.find('div', 'recruit')

            info = {}
            info['href'] = href
            info['src'] = src
            info['title'] = title.text
            info['description'] = description.text


            apply_num = recruit.text.split('/')[0]
            info['recruit'] = apply_num

            if minus_day == 'day':
                info['d_day'] = today.strftime('%Y-%m-%d')
            else:
                int_minus_day = int(minus_day)
                result_day = today - timedelta(days=int_minus_day)
                info['d_day'] = result_day.strftime('%Y-%m-%d')
        

        all_campaigns.append(info)

    

    return all_campaigns
    


    