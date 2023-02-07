from okx_candle import Market
from pprint import pprint

if __name__ == '__main__':
    # 币币交易：SPOT；永续合约：SWAP；交割合约：FUTURES；期权：OPTION
    instType = 'SWAP'
    # 实例化行情Market
    market = Market(instType)
    # 可以交易的产品列表
    pprint(market.get_symbols_trading_on())
    # 不可以交易的产品列表
    pprint(market.get_symbols_trading_off())
