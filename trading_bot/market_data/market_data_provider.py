import threading

from trading_bot.data.enums.exchanges import Exchanges
from trading_bot.data.enums.intervals import Intervals
from trading_bot.data.ticker import Ticker
from trading_bot.market_data.websocket_client import WebsocketClient


class MarketDataProvider(WebsocketClient):

    def __init__(self, tickers: list[Ticker], exchange: Exchanges, interval: Intervals):
        super().__init__(self._generate_url(tickers, exchange, interval))
        self._tickers = tickers
        self._thread = threading.Thread(target=super().run).start()

    def _generate_url(
        self, tickers: list[Ticker], exchange: Exchanges, interval: Intervals
    ) -> str:
        pass

    def _on_message(self, ws, message):
        print(f"{message=}")

    def stop(self):
        self.stopped = True
        self.ws.close()

    @property
    def tickers(self):
        return self._tickers

    @property
    def thread(self):
        return self._thread
