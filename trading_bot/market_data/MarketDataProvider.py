import threading

from trading_bot.data.enums.Exchanges import Exchanges
from trading_bot.data.ticker import Ticker
from trading_bot.market_data.WebsocketClient import WebsocketClient


class MarketDataProvider(WebsocketClient):

    def __init__(self, tickers: list[Ticker], exchange: Exchanges):
        super().__init__(self._generate_url(tickers, exchange))
        self._tickers = tickers
        self._thread = threading.Thread(target=super().run).start()

    def _generate_url(self, tickers: list[Ticker], exchange: Exchanges) -> str:
        pass

    def _on_message(self, ws, message):
        print(f"{message=}")

    @property
    def tickers(self):
        return self._tickers

    @property
    def thread(self):
        return self._thread
