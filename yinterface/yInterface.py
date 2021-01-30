import yfinance as yf
import pprint
import os
import pandas


def get_ticker_info(list_tickers = [], period = "5y"):

    ticker_info = {}
    for ticker in list_tickers:
        msft = yf.Ticker(ticker)
        ticker_info[ticker]={}

        # get stock info
        ticker_info[ticker]["stock_info"] = msft.info

        # get historical market data
        hist = msft.history(period=period)
        ticker_info[ticker]["hist_market_data"] = hist

        # show actions (dividends, splits)
        ticker_info[ticker]["actions"] = msft.actions

        # show dividends
        ticker_info[ticker]["dividends"] = msft.dividends

        # show splits
        ticker_info[ticker]["splits"] = msft.splits

        # show financials
        ticker_info[ticker]["financials"] = msft.financials
        ticker_info[ticker]["quarterly_financials"] = msft.quarterly_financials

        # show major holders
        ticker_info[ticker]["major_holders"] = msft.major_holders

        # show institutional holders
        ticker_info[ticker]["institutional_holders"] = msft.institutional_holders

        # show balance sheet
        ticker_info[ticker]["balance_sheet"] = msft.balance_sheet
        ticker_info[ticker]["quarterly_balance_sheet"] = msft.quarterly_balance_sheet

        # show cashflow
        ticker_info[ticker]["cashflow"] = msft.cashflow
        ticker_info[ticker]["quarterly_cashflow"] = msft.quarterly_cashflow

        # show earnings
        ticker_info[ticker]["earnings"] = msft.earnings
        ticker_info[ticker]["quarterly_earnings"] = msft.quarterly_earnings

        # show sustainability
        ticker_info[ticker]["sustainability"] = msft.sustainability

        # show analysts recommendations
        ticker_info[ticker]["recommendations"] = msft.recommendations

        # show next event (earnings, etc)
        ticker_info[ticker]["calendar"] = msft.calendar

        # show ISIN code - *experimental*
        # ISIN = International Securities Identification Number
        ticker_info[ticker]["isin"] = msft.isin
    return ticker_info



def dump_yfinanze(list_tickers, path):
    for ticker, value in list_tickers.items():
        new_dict = {}
        for key, factor in  value.items():
            if isinstance(factor, pandas.DataFrame) :
                new_dict[key] = factor.to_dict('records')
            elif isinstance(factor, pandas.Series):
                new_dict[key] = factor.to_dict()
            else:
                new_dict[key]= factor
        with open(os.path.join(path, ticker+".pprint"), 'w') as f:
            pprint.pprint(new_dict, f)

if __name__=="__main__":
    dump_yfinanze(get_ticker_info(['MAP.MC']), "d:\\tmp\\dumps")




