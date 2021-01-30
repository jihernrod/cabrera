

def dividend(value):
    import marketApi.dividend as dividend
    return dividend.dividend(value)


def get_spot(value):
    import marketApi.spots as spots
    return spots.get_spot(value)


def get_stock_return(spots_df):
    import marketApi.stock_returns as stock_returns
    return stock_returns.get_stock_return(spots_df)
