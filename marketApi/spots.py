
import copy
from pandas import DataFrame
import math


class AvgMovil:
    def __init__(self):
        self._avg_list = []
        self._avg_value = 0.0


    def add(self, value):
        self._avg_list.append(value)
        self._avg_value += value

    def calculate(self):
        value = self._avg_list.pop(0)
        self._avg_value -= value
        return self._avg_value / len(self._avg_list)

def get_spot(ticker_info):

    ticker_info_with_avg= {}

    for ticker, value in ticker_info.items():

        hist_market_data = value["hist_market_data"].reset_index()

        avg_50 = AvgMovil()
        avg_200 = AvgMovil()
        avg_1000 = AvgMovil()


        counter = 0

        copy_hist_market_data = copy.deepcopy(hist_market_data.values.tolist())

        for index, element in enumerate(hist_market_data.values.tolist(), start=0):

            quote = element[4]

            if math.isnan(quote):
                continue

            avg_50.add(quote)
            avg_200.add(quote)
            avg_1000.add(quote)


            if counter >= 50:
                copy_hist_market_data[index].append(avg_50.calculate())
            else:
                copy_hist_market_data[index].append(quote)


            if counter >= 200:
                copy_hist_market_data[index].append(avg_200.calculate())
            else:
                copy_hist_market_data[index].append(quote)


            if counter >= 1000:
                copy_hist_market_data[index].append(avg_1000.calculate())

            else:
                copy_hist_market_data[index].append(quote)

            counter += 1

        ticker_new_df = DataFrame(copy_hist_market_data,
                                  columns= ["Date","Open","High","Low","Close","Volume","Dividends",
                                           "Stock Splits","avg_50", "avg_200", "avg_1000" ])

        value["hist_market_data"] =  ticker_new_df


