import yfinance as yf
import pprint
import os
import pandas
import json

def addTicker(df, ticker):
    if isinstance(df, pandas.DataFrame):
        df["ticker"]= ticker
    elif isinstance(df, pandas.Series):
        df = df.to_frame()
        df["ticker"] = ticker
    elif isinstance(df, list):
        df["ticker"].append(ticker)
    elif isinstance(df, dict):
        df = pandas.Series(df).to_frame().T
        df["ticker"] = ticker
    return df


def get_ticker_info(list_tickers = [], period = "5y"):

    ticker_info = {}
    for ticker in list_tickers:
        msft = yf.Ticker(ticker)
        ticker_info[ticker]={}

        # get stock info
        ticker_info[ticker]["stock_info"] = addTicker(msft.info, ticker)

        # get historical market data
        hist = msft.history(period=period)

        ticker_info[ticker]["hist_market_data"] = addTicker(hist, ticker)
        ticker_info[ticker]["actions"] = addTicker(msft.actions, ticker)
        ticker_info[ticker]["dividends"] = addTicker(msft.dividends, ticker)
        ticker_info[ticker]["splits"] = addTicker(msft.splits, ticker)
        ticker_info[ticker]["financials"] = addTicker(msft.financials.T, ticker)
        ticker_info[ticker]["quarterly_financials"] = addTicker(msft.quarterly_financials.T, ticker)
        ticker_info[ticker]["major_holders"] = addTicker(msft.major_holders, ticker)
        ticker_info[ticker]["institutional_holders"] = addTicker(msft.institutional_holders, ticker)
        ticker_info[ticker]["balance_sheet"] = addTicker(msft.balance_sheet.T, ticker)
        ticker_info[ticker]["quarterly_balance_sheet"] = addTicker(msft.quarterly_balance_sheet.T, ticker)
        ticker_info[ticker]["cashflow"] = addTicker(msft.cashflow.T, ticker)
        ticker_info[ticker]["quarterly_cashflow"] = addTicker(msft.quarterly_cashflow.T, ticker)
        ticker_info[ticker]["earnings"] = addTicker(msft.earnings, ticker)
        ticker_info[ticker]["quarterly_earnings"] = addTicker(msft.quarterly_earnings, ticker)
        ticker_info[ticker]["sustainability"] = addTicker(msft.sustainability, ticker)
        ticker_info[ticker]["recommendations"] = addTicker(msft.recommendations, ticker)

        if msft.calendar is not None:
            ticker_info[ticker]["calendar"] = addTicker(msft.calendar.T, ticker)

        ticker_info[ticker]["isin"] = addTicker(msft.isin, ticker)
    return ticker_info


import os
def dump_yfinanze(list_tickers, path):

    dataframe_by_key = {}

    for ticker, value in list_tickers.items():
        new_dict = {}
        for key, factor in  value.items():
            if isinstance(factor, pandas.DataFrame) :
                if not key in dataframe_by_key:
                    dataframe_by_key[key] = factor
                else:
                    dataframe_by_key[key] = dataframe_by_key[key].append(factor)

            elif isinstance(factor, pandas.Series):
                new_dict[key] = json.loads( factor.to_json(orient="columns", date_format='iso') )
            else:
                new_dict[key]= factor
        with open(os.path.join(path, ticker+".pprint"), 'w') as f:
            pprint.pprint(new_dict, f)

    for key , df in dataframe_by_key.items():
        dataframe_by_key[key].to_csv(os.path.join("d:\\tmp\\dumps", key), date_format='%Y-%m-%d', index_label="index")


if __name__=="__main__":
    dump_yfinanze(get_ticker_info(["REE.MC", "ENG.MC", "MAP.MC"]), "d:\\tmp\\dumps")




