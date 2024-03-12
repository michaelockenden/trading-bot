import time

from trading_bot.client.binance_client import BinanceClient
from trading_bot.data.enums.interval import Interval
from trading_bot.data.models.ticker import Ticker
from trading_bot.market_data.binance_market_data_server import BinanceMarketDataServer
from trading_bot.market_data.websocket_client import WebsocketClient
from trading_bot.utils.file_utils import project_root


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
    BinanceMarketDataServer(project_root() / "trading_bot/market_data/csv.csv")
    # time.sleep(5)
    # WebsocketClient("ws://127.0.0.1:5000").run()


if __name__ == "__main__":
    main2()
