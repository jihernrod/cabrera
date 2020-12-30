from yinterface import yInterface
from marketApi import dividend, spots, stock_returns

import pprint

value = yInterface.get_ticker_info(list_tickers=["KO", "TEF.MC", "ENG.MC", "MAP.MC", "MSFT", "JNJ", "AWK", "CSCO"])
dividend_csv = dividend.dividend(value)

dividend_csv.to_csv("c:\\tmp\\dividend.csv")
spots_df = spots.get_spot(value)
spots_df = stock_returns.get_stock_return(spots_df)

for k, v in spots_df.items():
    v.to_csv("c:\\tmp\\%s_ticker.csv" % (k))


