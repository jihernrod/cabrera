

def dividend(ticker_info):

    result_df = None
    for ticker, value in ticker_info.items():

        value = value["dividends"].to_frame().reset_index()
        dividend_groupped = value.groupby(value["Date"].dt.year)['Dividends'].agg(['sum'])
        dividend_groupped = dividend_groupped.rename(columns={'sum': ticker})

        if result_df is None:
            result_df = dividend_groupped
        else:
            result_df = result_df.join(dividend_groupped)
    return result_df
