
from findash.data import TickerData
from findash.data import FredData
from findash.data import GDPData
from findash.data import DFII10Data


from datetime import date
from datetime import datetime
from dateutil.relativedelta import relativedelta
from termcolor import colored, cprint
from tabulate import tabulate

import os 
from dotenv import load_dotenv

load_dotenv()


def stock_line_data(ticker):
    line = []
    line.append(ticker)

    tick = TickerData(ticker,370)


    # Last price
    last_price = tick.last_price()
    if last_price == None:
        last_price = 'na'
    line.append(str(last_price))

    # Price history 
    l = []
    for v in tick.price_history():
        if v < 0:
            l.append(red(v))      
        else:
            l.append(green(v))      
    line.append("/".join(str(z) for z in l ))


    # MACD
    l = []
    macd, signal = tick.macd()
    if signal < 0 and signal < macd:
        l = [left_padding(macd), red(signal)]  
    else:
        l = [left_padding(macd), green(signal)]  
    line.append("/".join(str(z) for z in l ))


    # Bolinger
    l = []
    low, mid, high = tick.bolinger()
    if last_price != 'na':
        if mid > last_price:
            mid = red(mid)

        if low > last_price:
            low = red(low)
        
        if last_price > high:
            high = green(high)
    l = [low, mid, high] 
    line.append("/".join(str(z) for z in l ))

    # RSI
    rsi = tick.rsi()
    if rsi > 50:
        line.append(green(rsi))
    else:
        line.append(red(rsi))

    # Volume
    l = []
    for v in tick.vol_history():
        if v < 0:
            l.append(green(v))      
        else:
            l.append(red(v))      
    line.append("/".join(str(z) for z in l ))

    return line

def stock_line_header():
    return ['Ticker', 'Last', '1d/1w/1m/3m/1y', 'macd/sig', 'low/mid/high', 'rsi', 'volume 1d/1w/1m/3m']
            
def red(v):
    v = left_padding(v)
    return colored(v,'red',attrs=['reverse', 'blink'])
            
def green(v):
    v = left_padding(v)
    return colored(v,'green',attrs=['reverse', 'blink'])

def left_padding(v,pad=6):
    return ('{: >6}'.format(str(v)))

#####
def stock_watch(tickers=[]):
    all_data = []

    all_data.append(stock_line_header())
    for tick in tickers:
        d = stock_line_data(tick)

        all_data.append( d )

    print(tabulate(all_data,headers='firstrow'))


print("\n")
print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
index = {
    "VIX" : "^VIX",
    "GVZ" : "^GVZ"
}


stock = {
    "Mag7": ['AAPL', 'MSFT', 'AMZN', 'GOOG', 'META', 'TSLA', 'NVDA'],
    "Sector": ['SPY', 'QQQ','XLV','XLU','XLP','XLRE','XLC','XLF','XLK','XLY','XLE', 'XLB', 'XLI', 'ITA', 'IYR', 'SOXX'],
    "Speciality" : ['MGK', 'VIG'],
    "Commodity": ['GLDM', 'SLV', 'PPLT', 'CPER', 'URA', 'UNG', 'USO'],
    "Currency": ['BTC-USD','ETH-USD','UUP'],
    "Fixed_Income": ['SHY', 'IEI', 'IEF', 'TLT', 'SLQD'],
    "Country": ['EWC','KWEB', 'INDA', 'EWJ', 'EEM', 'EMXC', 'ACWX'],
    "Index": ["CL=F","NG=F"]
}

for key in stock:
    print("-->",key)
    stock_watch(stock[key])
    print("\n")


for key in index:
    print(" ",key," ", TickerData(index[key]).last_price(),end='')
print("\n")
