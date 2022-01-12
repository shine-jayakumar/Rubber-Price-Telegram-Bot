# Rubber Price Bot v.1

# Telegram bot that gets the current rubber price for Kottayam and Kochi

# copyright (c) 2022 Shine Jayakumar

from flask import Flask, request, Response
from flask_cors import CORS
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import os

app = Flask(__name__)
CORS(app)


token = os.getenv('TOKEN')


def extract_rubber_price(div_content):
    '''
    Extract rubber catergory and price from <td> elements
    from div passed
    '''
    rubber_cat = div_content.find_all('tr')
    rubber_price = {}
    for row in range(1, len(rubber_cat)):
        cols = rubber_cat[row].find_all('td')
        rubber_type = cols[0].text.replace(u'\xa0', '')
        price = cols[1].text.replace(u'\xa0', '')
        rubber_price[rubber_type] = float(price)/100
    return rubber_price


def format_price(heading, price_dict):
    '''
    Returns a formatted string while extracting rubber price
    from a dict containing rubber type and price
    
    Output:
    Kottayam:
    RSS4 - 160.5
    RSS5 - 156.0
    ISNR20 - 147.0
    Latex(60%) - 131.05
    '''
    frmtd_price = heading + "\n" + "\n".join([f"{key} - {val}" for key,val in price_dict.items()])
    return frmtd_price


def get_current_rubber_price():
    '''
    Extracts rubber price from the website
    and returns a formatted string containing 
    both Kottayam and Kochi rubber price
    '''
    URL = "http://rubberboard.org.in/public"
    kottayam_rubber_price = {}
    kochi_rubber_price = {}

    try:
        response = requests.get(URL)
        soup = BeautifulSoup(response.content, 'html.parser')

        kottayam_div = soup.find('div', {'id':'loc1'})
        kochi_div = soup.find('div', {'id':'loc2'})

        kottayam_rubber_price = extract_rubber_price(kottayam_div)
        kochi_rubber_price = extract_rubber_price(kochi_div)

        return f"{format_price('Kottayam:', kottayam_rubber_price)}\n\n{format_price('Kochi:', kochi_rubber_price)}"

    except:
        return False


def send_message(chat_id, msg):
    '''
    Sends message to user
    '''
    api_url = f'https://api.telegram.org/bot{token}/sendMessage'
    payload = {'chat_id': chat_id, 'text': msg}
    requests.post(api_url, json=payload)
   

@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        response = request.get_json()
        first_name = response['message']['chat']['first_name']
        chat_id = response['message']['chat']['id']
        today_dt = datetime.now().strftime("%d-%m-%Y")
        rubber_price = get_current_rubber_price()
        msg = ""
        if rubber_price:
            msg = f"Hi {first_name}\n\nRubber price as of {today_dt}:\n\n{rubber_price}"
        else:
            msg = f"Hi {first_name}. We could not get the rubber prices for today. We regret the inconvenience."
        send_message(chat_id, msg)
        return Response('Ok', status=200)
        
    else:
        return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Rubber Price Bot</title>
    </head>
    <body style="font-family: Arial">
        <h3>Rubber Price Telegram Bot v.1</h3>
        <h5>Copyright (c) 2022 Shine Jayakumar</h5>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=False, port=8080)