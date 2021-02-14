
class GetDashBoardAction:
    def __init__(self): pass

    def do(self):

        import service.generateRawInfo as generateRawInfoModule
        import configuration.config as config_interface
        import yinterface.yInterface as md_interface
        import marketApi.algoritms as algorithms_interface


        ret = {}
        stock_info = generateRawInfoModule.GenerateRawInfo(config_interface,
                                                      md_interface,
                                                      algorithms_interface).do()
        for key, value in stock_info.items():

            historic_market_data = value["hist_market_data"].to_dict("records")[-1]

            finance_info = {
                "Symbol": value["stock_info"]['symbol'],
                "BPA": value["stock_info"]['forwardEps'],
                "PER": value["stock_info"]['forwardPE'],
                "CUR": value["stock_info"]['currency'],
                "Industry": value["stock_info"]['sector'],
                "Beta": value["stock_info"]["beta"],
                "Ebitda":value["stock_info"]["enterpriseToEbitda"],
                "Payout":value["stock_info"]["payoutRatio"],
                "Close": value["stock_info"]["previousClose"],
                "Close_1000": historic_market_data["avg_1000"],
                "Close_200": historic_market_data["avg_200"],
                "Close_50": historic_market_data["avg_50"],
                "Rendimiento_1000": historic_market_data["returns_avg_1000"]
            }

            ret[key] =finance_info

        return ret

