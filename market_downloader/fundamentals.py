import requests
import pandas as pd
import time
import os
import datetime

import configuration.config as default_configuration

stock_list = default_configuration.get("Stocks")

now = datetime.datetime.now()
day_str = now.strftime("%Y%m%d")


class NotReturnData(Exception):
    pass


def download_fundamental_data(fundatmental_url, fundamental_file_name, output_adapter_functor = None):
    list_stocks = []
    for stock in stock_list:
        print("Getting info [%s] of [%s]" % (fundatmental_url, stock))
        response = requests.get(
                                 fundatmental_url % stock, verify=False)
        if output_adapter_functor:
            try:
                list_stocks.extend(output_adapter_functor(response.json()))
            except NotReturnData as nrd:
                print ("Err: %s %s %s"% ( stock, str(nrd), response.text ) )
        else:
            list_stocks.append(response.json())
        time.sleep(default_configuration.get("Download_Delay"))
    dataframe = pd.DataFrame(list_stocks)
    file_name = fundamental_file_name % (day_str)
    dataframe.to_csv(
                    os.path.join(default_configuration.get("Download_folder"), file_name))
    print("Export info [%s]" % file_name)


def adapter_annual_reports(x):
    if "annualReports" not in x:
        raise NotReturnData("Data is not completed")
    for report in x["annualReports"]:
        report["symbol"] =x["symbol"]
    return x["annualReports"]


def adapter_annual_earnings(x):
    if "annualEarnings" not in x:
        raise NotReturnData("Data is not completed")
    for report in x["annualEarnings"]:
        report["symbol"] = x["symbol"]
    return x["annualEarnings"]


if __name__ == "__main__":

    urls = ["IncomeStatement_url",
            "BalanceSheet_url",
            "CashFlow_url"]

    files_to_export = [
            "IncomeStatement_file_name",
            "BalanceSheet_file_name",
            "CashFlow_file_name"]

    for url, file in zip(urls, files_to_export):
       download_fundamental_data(default_configuration.get(url),
                                 default_configuration.get(file), output_adapter_functor=lambda x: adapter_annual_reports(x))

    download_fundamental_data(default_configuration.get("Earnings_url"),
                              default_configuration.get("Earnings_file_name"), output_adapter_functor=lambda x: adapter_annual_earnings(x))

    download_fundamental_data(default_configuration.get("Fundamental_url"),
                              default_configuration.get("Fundamental_file_name"))

