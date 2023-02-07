from okx_candle import Market
from pprint import pprint

if __name__ == '__main__':
    # 币币交易：SPOT；永续合约：SWAP；交割合约：FUTURES；期权：OPTION
    instType = 'SWAP'
    # 实例化行情Market
    market = Market(instType)
    # 产品类型的全部交易规范
    exchangeInfos = market.get_exchangeInfos()
    pprint(exchangeInfos)
    # BTC-USDT-SWAP的交易规范（BTC-USDT-SWAP属于永续合约产品）
    BTC_USDT_SWAP_enchangeInfo = market.get_exchangeInfo('BTC-USDT-SWAP')
    pprint(BTC_USDT_SWAP_enchangeInfo)
