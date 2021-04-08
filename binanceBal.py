import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from binance.client import Client
import configparser
from binance.websockets import BinanceSocketManager
import time
import os

##############################################################################
# Loading keys from config file
api_key = os.environ.get('binance_api')
api_secret = os.environ.get('binance_secret')

#api_key,api_secret
client = Client(api_key, api_secret)
client.API_URL = 'https://api.binance.us/api'


#print(avg_price)
# Setting up connection

info = client.get_account()  # Getting account info
prices = client.get_all_tickers() #get current price data

dict(prices)

#print(prices)

assets = []
values = []
for index in range(len(info['balances'])):
    for key in info['balances'][index]:
        if key == 'asset':
            assets.append(info['balances'][index][key])
        if key == 'free':
            values.append(info['balances'][index][key])


token_usd = {}  # Dict to hold pair price in USD
token_pairs = []  # List to hold different token pairs

held_tokens = dict(zip(assets,values)) #combine the two 
valueToDel = '0.00000000'

# remove extra tokens that we dont have
held_tokens = {key:val for key, val in held_tokens.items() if val != valueToDel}
valueOfAssets = 0.0


#when this bit of code runs it takes the current prices and the coins in your account and calcualtes your account value in USD
for token in held_tokens:
    if token != 'USD':
        token_usd = token + 'USD'
        avg_price = client.get_avg_price(symbol=token_usd)
        valueOfAssets += float(avg_price['price']) * float(held_tokens[token])
        #print(valueOfAssets)

print('you have ', valueOfAssets, ' $ worth of cryptocurency in your binance account at current prices')
#print(valueOfAssets)


#print(held_tokens)



#print(assets,values)
#print(prices)


