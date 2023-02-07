from okx_candle import Market
from pprint import pprint


if __name__ == '__main__':
    # 币币交易：SPOT；永续合约：SWAP；交割合约：FUTURES；期权：OPTION
    instType = 'SWAP'
    # 实例化行情Market
    market = Market(instType)
    # 单个产品的深度信息（BTC-USDT-SWAP）sz：深度数量
    pprint(market.get_books('BTC-USDT-SWAP', sz=10))
    # 获取BTC-USDT-SWAP产品轻量深度
    pprint(market.get_books_lite(symbol='BTC-USDT-SWAP'))
