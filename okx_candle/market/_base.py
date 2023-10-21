from okx.market import Market
from okx.public import Public


class MarketBase():
    def __init__(
            self,
            instType: str,
            key: str = '',
            secret: str = '',
            passphrase: str = '',
            timezone='Asia/Shanghai',
            proxies={},
            proxy_host: str = None,
    ):
        self.instType = instType.upper()

        FLAG = '0'  # 实盘
        self.marketAPI = Market(
            key=key,
            secret=secret,
            passphrase=passphrase,
            flag=FLAG,
            proxies=proxies,
            proxy_host=proxy_host,
        )
        self.publicAPI = Public(
            key=key,
            secret=secret,
            passphrase=passphrase,
            flag=FLAG,
            proxies=proxies,
            proxy_host=proxy_host,
        )
        self.timezone = timezone
