import pprint
import os
import pandas

def dump(list_tickers, path):
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