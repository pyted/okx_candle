from okx_candle import Market
from pprint import pprint

if __name__ == '__main__':
    # 币币交易：SPOT；永续合约：SWAP；交割合约：FUTURES；期权：OPTION
    instType = 'SWAP'
    # 实例化行情Market
    market = Market(instType)
    # 全部产品的行情数据
    pprint(market.get_tickersMap())  # 字典类型
    pprint(market.get_tickers())  # 列表类型
    # 单个产品的行情数据（BTC-USDT-SWAP）
    pprint(market.get_ticker('BTC-USDT-SWAP'))

