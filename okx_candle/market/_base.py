from okx_api.market import Market
from okx_api.public import Public


# from okx_candle.api.Market_api import MarketAPI
# from okx_candle.api.Public_api import PublicAPI


class MarketBase():
    def __init__(
            self,
            instType: str,
            key: str = '',
            secret: str = '',
            passphrase: str = '',
            timezone='Asia/Shanghai'
    ):
        self.instType = instType.upper()
        FLAG = '0'  # 实盘
        self._marketAPI = Market(
            key=key,
            secret=secret,
            passphrase=passphrase,
            flag=FLAG
        )
        self._publicAPI = Public(
            key=key,
            secret=secret,
            passphrase=passphrase,
            flag=FLAG
        )
        self.timezone = timezone
