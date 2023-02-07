from okx_candle import CandleServer, CandleRule

if __name__ == '__main__':
    # 币币交易：SPOT；永续合约：SWAP；交割合约：FUTURES；期权：OPTION
    instType = 'SWAP'
    # 永续合约，默认规则
    candleServer = CandleServer(instType, CandleRule)
    # 每日在CandleRule.DOWNLOAD_TIME时刻开始下载前一日的历史K线
    candleServer.download_daily()
    # candleServer.close_download_daily() 关闭服务
