

def dividend(ticker_info):

    for ticker, value in ticker_info.items():

        value_dividends = value["dividends"].to_frame().reset_index()
        dividend_groupped = value_dividends.groupby(value_dividends["Date"].dt.year)['Dividends'].agg(['sum'])
        dividend_groupped = dividend_groupped.rename(columns={'sum': ticker})
        value["dividends_grouped"] = dividend_groupped

