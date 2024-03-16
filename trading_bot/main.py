from trading_bot.client.binance_client import BinanceClient
from trading_bot.data.enums.interval import Interval
from trading_bot.data.models.market_data import BinanceMarketData
from trading_bot.data.models.ticker import Ticker
from trading_bot.market_data.test_websocket_client import TestWebsocketClient


def main1():
    tickers = [Ticker("BTCUSDT"), Ticker("ETHUSDT"), Ticker("SOLUSDT")]
    interval = Interval.ONE_MINUTE
    b_client = BinanceClient(tickers, interval)
    provider = b_client.market_data_provider
    ticker = provider.get_ticker("BTCUSDT")
    ticker.wait_for_data(30)
    print(b_client.account_manager.get_account_value_usd())
    provider.stop()


def main2():
    TestWebsocketClient(BinanceMarketData).run()


if __name__ == "__main__":
    main1()
