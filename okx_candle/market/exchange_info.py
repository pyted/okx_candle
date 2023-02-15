import time
from okx_candle import code
from okx_candle.market._base import MarketBase


class ExchangeInfo(MarketBase):

    def get_exchangeInfos(self, expire_seconds: int = 60 * 5, uly: str = ''):
        '''
        :param expire_seconds: 缓存时间（秒）
        :param uly: 标的指数，仅适用于交割/永续/期权，期权必填
        使用的缓存数据格式：
            self._exchangeInfo_cache = [
                {
                    'code':<状态码>,
                    'data':<exchangeInfo数据>,
                    'msg':<提示信息>,
                },
                <上次更新的毫秒时间戳>
            ]
        '''

        if (
                # 无缓存数据
                not hasattr(self, '_exchangeInfo_caches')
                or
                # 缓存数据过期
                getattr(self, '_exchangeInfo_caches')[1] - time.time() * 1000 >= expire_seconds
        ):
            # 更新数据并设置时间戳
            setattr(self, '_exchangeInfo_caches',
                    [self.publicAPI.get_instruments(instType=self.instType, uly=uly), time.time() * 1000])
        # 返回缓存数据
        return getattr(self, '_exchangeInfo_caches')[0]

    def get_exchangeInfo(
            self,
            symbol: str,
            expire_seconds: int = 60 * 5,
            uly: str = '',
    ):
        '''
        :param symbol: 产品
        :param expire_seconds: 缓存时间（秒）
        :param uly: 标的指数，仅适用于交割/永续/期权，期权必填
        '''
        exchangeInfos_result = self.get_exchangeInfos(uly=uly, expire_seconds=expire_seconds)
        # [ERROR RETURN] 异常交易规则与交易
        if exchangeInfos_result['code'] != '0':
            return exchangeInfos_result
        # 寻找symbol的信息
        for symbol_data in exchangeInfos_result['data']:
            if symbol_data['instId'] == symbol:
                symbol_data = symbol_data
                break
        else:
            symbol_data = None
        # [ERROR RETURN] 没有找到symbol的交易规则与交易对信息
        if symbol_data == None:
            result = {
                'code': code.EXCHANGE_INFO_ERROR[0],
                'data': exchangeInfos_result['data'],
                'msg': f'Symbol not found symbol={symbol}'
            }
            return result
        # 将filters中的列表转换为字典，里面可能包含下单价格与数量精度
        result = {
            'code': '0',
            'data': symbol_data,
            'msg': '',
        }
        return result

    # 获取可以交易的产品列表
    def get_symbols_trading_on(
            self,
            expire_seconds: int = 60 * 5,
            uly: str = '',
    ) -> dict:
        '''
        :param expire_seconds: 缓存时间（秒）
        :param uly: 标的指数，仅适用于交割/永续/期权，期权必填
        '''
        exchangeInfos_result = self.get_exchangeInfos(uly=uly, expire_seconds=expire_seconds)
        # [ERROR RETURN] 异常交易规则与交易
        if exchangeInfos_result['code'] != '0':
            return exchangeInfos_result
        status_name = 'state'

        symbols = [
            data['instId']
            for data in exchangeInfos_result['data']
            if data[status_name] == 'live'
        ]
        # [RETURN]
        result = {
            'code': '0',
            'data': symbols,
            'msg': ''
        }
        return result

    # 获取不可交易的产品列表
    def get_symbols_trading_off(
            self,
            expire_seconds: int = 60 * 5,
            uly: str = '',
    ) -> dict:
        '''
        :param expire_seconds: 缓存时间（秒）
        :param uly: 标的指数，仅适用于交割/永续/期权，期权必填
        '''
        exchangeInfos_result = self.get_exchangeInfos(uly=uly, expire_seconds=expire_seconds)
        # [ERROR RETURN] 异常交易规则与交易
        if exchangeInfos_result['code'] != '0':
            return exchangeInfos_result
        status_name = 'state'

        symbols = [
            data['instId']
            for data in exchangeInfos_result['data']
            if data[status_name] != 'live'
        ]
        # [RETURN]
        result = {
            'code': '0',
            'data': symbols,
            'msg': ''
        }
        return result
