import time

from trading_bot.client.binance_client import BinanceClient
from trading_bot.data.enums.interval import Interval
from trading_bot.data.models.ticker import Ticker

if __name__ == "__main__":
    tickers = [Ticker("BTCUSDT"), Ticker("ETHUSDT"), Ticker("SOLUSDT")]
    interval = Interval.ONE_MINUTE
    b_client = BinanceClient(tickers, interval)
    provider = b_client.market_data_provider
    ticker = provider.get_ticker("BTCUSDT")
    ticker.wait_for_data(30)
    print(ticker.latest_market_data.close_price)
    provider.stop()
