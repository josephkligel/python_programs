#!/usr/bin/python3
import requests
import json
from colorama import Fore
from currencylist import check_list
from Tkinter import *

# def pl_color(num):
#     if(num > 0):
#         color = Fore.GREEN
#         return color
#     elif(num < 0):
#         color = Fore.RED
#         return color

limit = 5
# currency = check_list(input("What currency would you like to view (remember all caps) ? "))
currency = 'USD'
api_request = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit={}&convert={}&CMC_PRO_API_KEY=a4f4cb0a-d308-4307-8ad1-6796f1f869b5".format(limit, currency))

api = json.loads(api_request.content)

coins = [
    {
        'symbol': 'BTC',
        'amount_owned': 2,
        'price_per_coin': 3200
    },
    {
        'symbol': 'ETH',
        'amount_owned': 100,
        'price_per_coin': 2.05
    }
]

total_pl = 0
for i in range(0, 5):
    for coin in coins:
        if api['data'][i]['symbol'] == coin['symbol']:
            total_paid = coin['amount_owned'] * coin['price_per_coin']
            current_value = coin["amount_owned"] * api['data'][i]['quote']['USD']['price']
            pl_per_coin = api['data'][i]['quote']['USD']['price'] - coin['price_per_coin']
            total_pl_coin = pl_per_coin * coin['amount_owned']

            print(api['data'][i]['name'] + " - " + api['data'][i]['symbol'])
            print('Price - %.2f' % (api['data'][i]['quote'][currency]['price']))
            print('Number of coins:', coin['amount_owned'])
            print('Total Amount Paid: ${:,.2f}'.format(total_paid))
            print('Current Value: ${:,.2f}'.format(current_value))
            print('P/L per coin: ${:,.2f}'.format(pl_per_coin))
            print('Total P/L for coin: ${:,.2f}'.format(total_pl_coin))
            total_pl += total_pl_coin
            print("-----------------------------------------")

print("Total P/L for portfolio: ${:,.2f}".format(total_pl))
