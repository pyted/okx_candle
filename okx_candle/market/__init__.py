from okx_candle.market.exchange_info import ExchangeInfo
from okx_candle.market.ticker import Ticker
from okx_candle.market.history_candle import HistoryCandle


class Market(ExchangeInfo,Ticker,HistoryCandle):
    pass
