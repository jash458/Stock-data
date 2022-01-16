import yfinance as yf
import numpy as np
import pandas as pd


#defining function
def stock_data(list): 

    #empty dictionary in which we are going to add data-value of different stocks.
    dict_of_tickers={} #basically we going to make it nested-dictionary

    for ticker in list:
        #fetching stock data from site
        ticker_data = yf.download(f"{ticker}.NS", start="2021-01-01", end="2021-03-01", rounding='True')
        #converting data to dict.
        ticker_data = ticker_data.to_dict(orient='list')
        update_dict_of_tickers={f"{ticker}":ticker_data}
        #updating dict. by adding key-value pair from update_dict_of_tickers
        dict_of_tickers.update(update_dict_of_tickers)
     
    #print(dict_of_tickers.keys())


#taking stock name from user
symbols=input("Enter multiple Stocks Name:")
list_of_tickers = list(symbols.split(" "))
print(list_of_tickers) #passing list of tickers as arrgument
stock_data(list_of_tickers) #calling stock function
