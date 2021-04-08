from binance.client import Client
import os
import configparser
import pandas as pd
api_key = os.environ.get('binance_api')
api_secret = os.environ.get('binance_secret')

client = Client(api_key, api_secret)
client.API_URL = 'https://api.binance.us/api'

tickers = client.get_account()
balance = client.get_asset_balance(asset='ETH')

# Getting earliest timestamp availble (on Binance)
earliest_timestamp = client._get_earliest_valid_timestamp('ETHUSDT', '1d')  # Here "ETHUSDT" is a trading pair and "1d" is time interval
print(earliest_timestamp)

# Getting historical data (candle data or kline)
candle = client.get_historical_klines("ETHUSDT", "1d", earliest_timestamp, limit=1000)

print(candle[1])
#print(balance)

eth_df = pd.DataFrame(candle, columns=['dateTime', 'open', 'high', 'low', 'close', 'volume', 'closeTime', 'quoteAssetVolume', 'numberOfTrades', 'takerBuyBaseVol', 'takerBuyQuoteVol', 'ignore'])
eth_df.dateTime = pd.to_datetime(eth_df.dateTime, unit='ms')
eth_df.closeTime = pd.to_datetime(eth_df.closeTime, unit='ms')
eth_df.set_index('dateTime', inplace=True)
eth_df.to_csv('eth_candle.csv')

print(eth_df.tail(10))