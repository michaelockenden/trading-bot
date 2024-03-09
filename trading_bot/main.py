import time

from trading_bot.client.binance.binance_client import BinanceClient

if __name__ == "__main__":
    b_client = BinanceClient()
    time.sleep(30)
    b_client.market_data_provider.stop()
