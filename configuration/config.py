CONF ={
    "Stocks": ["T", "LOG.MC", "INTC", "BN.PA", "ENG.MC", "BBVA.MC", "NTGY.MC", "TEF.MC", "MAP.MC", "CSCO", "KO"],

    "Fundamental_url": "https://www.alphavantage.co/query?function=OVERVIEW&symbol=%s&apikey=G762XMM5O6NTMLMI",
    "IncomeStatement_url": "https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol=%s&apikey=G762XMM5O6NTMLMI",
    "BalanceSheet_url": "https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol=%s&apikey=G762XMM5O6NTMLMI",
    "CashFlow_url": "https://www.alphavantage.co/query?function=CASH_FLOW&symbol=%s&apikey=G762XMM5O6NTMLMI",
    "Earnings_url": "https://www.alphavantage.co/query?function=EARNINGS&symbol=%s&apikey=G762XMM5O6NTMLMI",

    "Fundamental_file_name": "fundamental_%s.csv",
    "IncomeStatement_file_name": "incomeStatement_%s.csv",
    "BalanceSheet_file_name": "balanceSheet_%s.csv",
    "CashFlow_file_name": "cashFlow_%s.csv",
    "Earnings_file_name": "earnings_%s.csv",

    "Download_folder": "D:\\tmp",
    "Download_Delay": 15
}



def get(key, default_value = None):
    return CONF.get(key, default_value)
