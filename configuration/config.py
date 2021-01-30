CONF ={
    "Stocks": ["T", "LOG.MC", "INTC", "BN.PA", "ENG.MC", "BBVA.MC", "NTGY.MC", "TEF", "MAP.MC", "CSCO", "KO"]
}



def get(key, default_value = None):
    return CONF.get(key, default_value)
