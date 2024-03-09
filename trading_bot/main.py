import time

from trading_bot.client.binance.binance_client import BinanceClient
from trading_bot.data.ticker import Ticker

if __name__ == "__main__":
    tickers = [Ticker("BTCUSDT"), Ticker("ETHUSDT"), Ticker("SOLUSDT")]
    b_client = BinanceClient(tickers)
    time.sleep(30)
    b_client.market_data_provider.stop()
