import pickle
import pandas as pd
import requests as r
import json
from lxml import html
import numpy as np
import datetime as dt
import sys
import holidays
import os
import matplotlib.dates as mdates
from bs4 import BeautifulSoup

if __name__=="__main__":

    swedish_holidays = holidays.Sweden()
    closing_time = dt.time(16,00,00)
    wait_for_market = 30

    start_date = dt.date(2000, 1, 1)

    # sync_url = 'http://www.nasdaqomxnordic.com/shares/listed-companies/stockholm'
    sync_html = "data/swedish_stocks.html"

    with open(sync_html, 'r') as fp:
        soup = BeautifulSoup(fp, 'html.parser')

    rows = soup.find_all('tr')

    ticker_data = {}
    for row in list(rows[1:]):
        entry = list(filter(lambda r: r != "\n", list(row.children)[:4]))
        ticker_data["-".join(f"{entry[1].text}.ST".split(" "))] = entry[0].text

    filename = "data/swedish_tickers.p"
    outfile = open(filename, 'wb')
    pickle.dump(ticker_data, outfile)
    outfile.close()