# All required dependencies
import os
import requests
import time
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from datetime import datetime
import nexmo
from dotenv import load_dotenv
import argparse
# TO load enviourmental variables
load_dotenv()

# various parameter for sms service

NEXMO_BRAND_NAME = os.getenv("BRAND_NAME")
TO_NUMBER = os.getenv("NUMBER")
NEXMO_API_KEY = os.getenv("API_KEY")
NEXMO_API_SECRET = os.getenv("API_SECRET")
client = nexmo.Client(key=NEXMO_API_KEY, secret=NEXMO_API_SECRET)

# API and HEADERS

COINMARKET_API_URL = os.getenv("API_URL")
parameters = {
  'start': '1',
  'limit': '1',
  'convert': 'INR'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '7b71e96b-e81b-4fd5-8a18-99c89ffae3f9',
}

session = Session()
session.headers.update(headers)

# IFTTT URL
IFTTT_WEBHOOKS_URL = os.getenv("IFTTT")

parser = argparse.ArgumentParser(
    description="Bitcoin Notifier"
)
parser.add_argument('app', type=str)
args = parser.parse_args()


# Function to get latest bitcoin prices


def LatestBitcoinPrice():
    try:
        # here we use try and except method
        response = session.get(COINMARKET_API_URL, params=parameters)
        # to make get request from api
        respons_json = json.loads(response.text)
        # saving response from api
        return respons_json['data'][0]['quote']['INR']['price']
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)


# Function to use IFTTT applets

def IftttPost(event, value):
    # to trigger ifttt webhooks
    data = {'value1': value}
    ifttt_event_url = IFTTT_WEBHOOKS_URL.format(event)
    requests.post(ifttt_event_url, json=data)


price1 = LatestBitcoinPrice()
# get bitcoin price to send it via sms

print(price1)

# commands to send sms for alert
responseData = client.send_message(
    {
        "from": NEXMO_BRAND_NAME,
        "to": TO_NUMBER,
        "text": "Latest Bitcoin Price is: Rs.{}".format(price1),
          }
)

if responseData["messages"][0]["status"] == "0":
    print("Message sent successfully.")
else:
    print(f"Message failed error: {responseData['messages'][0]['error-text']}")


def formatHistory(bitcoin_history):
    lines = []
    for price in bitcoin_history:
        # string in order of day, month, year, hour and minute
        date, price = price['date'].strftime('%d.%m.%Y %H:%M'), price['price']
        # To get notifications of full history of price with date
        # Date format is day, month, year, hour and minute
        line = 'on {}:price is ₹{}'.format(date, price)
        lines.append(line)
    # join will used to join lines as line1<br>line2<br>line3
    return '<br>'.join(lines)  # <br> for creating new line.


thresholdPrice = 760000


def mainFunc():
    bitcoin_history = []
    while True:
        price, date = LatestBitcoinPrice(), datetime.now()
        bitcoin_history.append({'date': date, 'price': price})
        # IF price is less than threshold price
        # To send bitcoin price alert on ifttt app, Twitter and Email.
        # Event Name- 'bitcoin_price_emergency'
        if price < thresholdPrice:
            if args.app == "ifttt":
                # For alert on IFTTT app
                IftttPost('bitcoin_price_ifttt', price)
            elif args.app == "email":
                # For alert on Email
                IftttPost('bitcoin_price_email', price)
            elif args.app == "twitter":
                # For alert on Twitter
                IftttPost('bitcoin_price_twitter', price)
        # For sending 3 consicutive alert of bitcoin price
        if (len(bitcoin_history) == 3):  # for maximum lines of 3 notifications
            # To send alert on Slack Workspace Bitcoin InFO.
            # Event Name- 'bitcoin-price-update'
            IftttPost('bitcoin_price_update', formatHistory(bitcoin_history))
            # delete history and reset it to empty
            bitcoin_history = []
        # Sleep for 10 seconds
        # Both event will trigger after each 10 sec.
        time.sleep(10)


if __name__ == '__main__':
    mainFunc()
