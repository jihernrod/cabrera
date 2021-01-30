

class GenerateRawInfo:
    def __init__(self,  conf_interface,
                        md_interface,
                        algorithms_interface):

        self.__md_interface = md_interface
        self.__conf_interface = conf_interface
        self.__algorithms_interface =algorithms_interface

    def do(self):
        list_stocks = self.__conf_interface.get("Stocks")
        value = self.__md_interface.get_ticker_info(list_tickers=list_stocks)
        self.__algorithms_interface.dividend(value)
        self.__algorithms_interface.get_spot(value)
        self.__algorithms_interface.get_stock_return(value)

        return value

