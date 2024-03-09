import threading

from trading_bot.data.enums.exchange import Exchange
from trading_bot.data.enums.interval import Interval
from trading_bot.data.models.ticker import Ticker
from trading_bot.market_data.websocket_client import WebsocketClient
from trading_bot.utils.logging import TradingBotLogger


class MarketDataProvider(WebsocketClient):

    def __init__(self, tickers: list[Ticker], exchange: Exchange, interval: Interval):
        super().__init__(self._generate_url(tickers, exchange, interval))
        self._tickers = tickers
        self._thread = threading.Thread(target=super().run).start()
        self._logger = TradingBotLogger(self.__class__.__name__).get_logger()

    def _generate_url(
        self, tickers: list[Ticker], exchange: Exchange, interval: Interval
    ) -> str:
        pass

    def _on_message(self, ws, message):
        self._logger.info(f"{message=}")

    def stop(self):
        self.stopped = True
        self.ws.close()

    @property
    def tickers(self):
        return self._tickers

    @property
    def thread(self):
        return self._thread
