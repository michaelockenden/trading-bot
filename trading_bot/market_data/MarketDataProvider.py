import threading

from trading_bot.data.enums.Exchanges import Exchanges
from trading_bot.market_data.WebsocketClient import WebsocketClient


class MarketDataProvider(WebsocketClient):

    def __init__(self, tickers: tuple[str, ...], exchange: Exchanges):
        super().__init__(self._generate_url(tickers, exchange))
        self._tickers = tickers
        self._thread = threading.Thread(target=super().run).start()

    def get_thread(self) -> threading.Thread:
        return self._thread

    def get_tickers(self) -> tuple[str, ...]:
        return self._tickers

    def _generate_url(self, tickers: tuple[str, ...], exchange: Exchanges) -> str:
        pass

    def _on_message(self, ws, message):
        print(f"{message=}")

