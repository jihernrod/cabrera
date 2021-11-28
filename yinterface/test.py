import pandas as pd
import html5lib
from bs4 import BeautifulSoup
import requests
# Scrape the entire S&P500 list from Wikipedia into a Pandas DataFrame;
ticker_list = pd.read_html(
'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
df = (ticker_list[0].to_numpy()).tolist()

ticker = []
for l in df:
    ticker.append(l[0])


import yInterface

yInterface.dump_yfinanze(yInterface.get_ticker_info(ticker), "d:\\tmp\\dumps")

print(ticker)