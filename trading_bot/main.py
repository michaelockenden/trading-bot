import time

from trading_bot.client.binance.binance_client import BinanceClient
from trading_bot.data.enums.interval import Interval
from trading_bot.data.ticker import Ticker

if __name__ == "__main__":
    tickers = [Ticker("BTCUSDT"), Ticker("ETHUSDT"), Ticker("SOLUSDT")]
    interval = Interval.ONE_MINUTE
    b_client = BinanceClient(tickers, interval)
    time.sleep(30)
    b_client.market_data_provider.stop()
