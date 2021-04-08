from binance.client import Client
import os
import configparser
import pandas as pd
from binance.websockets import BinanceSocketManager
from twisted.internet import reactor 

api_key = os.environ.get('binance_api')
api_secret = os.environ.get('binance_secret')

client = Client(api_key, api_secret)
client.API_URL = 'https://api.binance.us/api'

def streaming_data_process(msg):
    """
    Function to process the received messages
    param msg: input message
    """
    print(f"message type: {msg['e']}")
    print(f"close price: {msg['c']}")
    print(f"best ask price: {msg['a']}")
    print(f"best bid price: {msg['b']}")
    print("---------------------------")
    
# Starting the WebSocket
bm = BinanceSocketManager(client)
conn_key = bm.start_symbol_ticker_socket('ETHUSDT', streaming_data_process)
bm.start()