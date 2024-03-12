import threading
import time
from abc import abstractmethod
from typing import Type
from abc import ABC, abstractmethod

from trading_bot.data.enums.exchange import Exchange
from trading_bot.data.enums.interval import Interval
from trading_bot.data.enums.time_units import TimeUnits
from trading_bot.data.models.market_data import MarketData
from trading_bot.data.models.ticker import Ticker
from trading_bot.market_data.websocket_client import WebsocketClient
from trading_bot.utils.logging import TradingBotLogger
from trading_bot.utils.num_utils import remove_trailing_zeroes


class MarketDataProvider(WebsocketClient, ABC):

    def __init__(
        self,
        tickers: list[Ticker],
        exchange: Exchange,
        interval: Interval,
        market_data_model: Type[MarketData],
    ):
        super().__init__(self._generate_url(tickers, exchange, interval))
        self._tickers = tickers
        self._exchange = exchange
        self._market_data_model = market_data_model
        self._thread = threading.Thread(target=super().run)
        self._thread.start()
        self._logger = TradingBotLogger("MarketDataProvider").get_logger()

    @abstractmethod
    def _generate_url(
        self, tickers: list[Ticker], exchange: Exchange, interval: Interval
    ) -> str: ...

    def _on_message(self, ws, message):
        received_time = time.time()
        market_data = self._market_data_model.model_validate_json(message)
        self.get_ticker(market_data.symbol).add_data(market_data)

        time_to_receive = received_time - (
            market_data.timestamp / TimeUnits.MILLIS_PER_SECOND.value
        )
        if time_to_receive > 0.5:
            self._logger.warning("Slow message")
        self._logger.info(
            f"{self._exchange.name}-{market_data.symbol} -> ${remove_trailing_zeroes(market_data.close_price)}"
            f" || time to receive message: {time_to_receive:.3f}s"
        )

    def stop(self):
        self.stopped = True
        self.ws.close()

    def get_ticker(self, symbol: str) -> Ticker | None:
        for ticker in self._tickers:
            if ticker.symbol == symbol.lower():
                return ticker
        return None

    @property
    def tickers(self):
        return self._tickers

    @property
    def thread(self):
        return self._thread
