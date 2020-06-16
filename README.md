# BITCOIN PRICE ALERT NOTIFIER WITH PYTHON

As we all know, Bitcoin price is a fickle thing. You never really know where it’s going to be at the end of the day. So, instead of constantly checking various sites for the latest updates, let’s make a Python app to do the work for you.

For this, we’re going to use the popular automation website IFTTT. IFTTT (“if this, then that”) is a web service that bridges the gap between different apps and devices.

We’re going to create these IFTTT applets:

- For emergency notification when Bitcoin price falls under a certain threshold.
- For regular Slack updates on the Bitcoin price.
- For making tweet on twitter regarding Bitcoin price.
- For regular update of Bitcoin price via Email.

We also used a platform called NEXMO to send alert of Bitcoin Price via SMS on a particular mobile number.


Both will be triggered by our Python app which will consume the data from the Coinmarketcap API.

An IFTTT applet is composed of two parts: a trigger and an action.

In our case, the trigger will be a webhook service provided by IFTTT. You can think of webhooks as “user-defined HTTP callbacks” and you can read more about them here.

Our Python app will make an HTTP request to the webhook URL which will trigger an action. Now, this is the fun part—the action could be almost anything you want. IFTTT offers a multitude of actions like sending an email, updating a Google Spreadsheet and even calling your phone.

Project Setup
## Getting Started

Before getting started make sure you have valid email-id, Mobile number and internet connection.

### | Prerequisites

- Python.
- Pip.
- NEXMO package.
- Requests library.
- OS

### | Installing

- Installing python : Link -> [Visit Website](https://www.codecademy.com/articles/install-python)

- Install NEXMO :

> pip install nexmo

- Install requests library

> pip install requests

- Install Dotenv

> pip install -U python-dotenv

- Clone or Download the Bitcoin-Notification repository on your local system

---

## Deployment

- Before deployment you need to create environment variables in your system where you will save various non shareble ID, password, API keys and URL. We are also saving our mobile number, NEXMO key and secret in a file named as .env.


- Open the folder in which you have clone the repository, press and hold shift and right-click. You will see option "Open command window here" click on that.

- For Phone number update one can change its phone number in ,env file.

- You just need to run the BitcoinNot.py file in your terminal and app will start it's work.

- Maximize the command prompt window in order to get better visualization. In command prompt type a command and press enter.


> python BitcoinNot


BitcoinNot.py

- After that Bitcoin Price Ticker app will launch, now just follow the instructions and enter your data as follows
 1 BitcoinNot.py ifttt  
 2 BitcoinNot.py email
 3 BitcoinNot.py twitter


- Make sure you enter the valid Email-id and Phone number, then your input data will be shown.


---

## Build with

| Python - High level programming language.

| API for bitcoin price - Link ->
[coinMarketApp]('https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest')

| IFTTT - Cloud communication platform.

| NEXMO - PLatform for SMS.

---

## Versioning

| We use git for version controlling and this is Version 01 .

---

## Author

| Rohan Sharma - [Profile](https://github.com/rohan-sharma-au6)

# Bitcoin
