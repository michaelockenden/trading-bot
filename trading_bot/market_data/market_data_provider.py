import threading
import time
from typing import Type

from trading_bot.data.enums.exchange import Exchange
from trading_bot.data.enums.interval import Interval
from trading_bot.data.enums.time_units import TimeUnits
from trading_bot.data.models.market_data import MarketData
from trading_bot.data.models.ticker import Ticker
from trading_bot.market_data.websocket_client import WebsocketClient
from trading_bot.utils.logging import TradingBotLogger


class MarketDataProvider(WebsocketClient):

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
        self._thread = threading.Thread(target=super().run).start()
        self._logger = TradingBotLogger("MarketDataProvider").get_logger()

    def _generate_url(
        self, tickers: list[Ticker], exchange: Exchange, interval: Interval
    ) -> str:
        pass

    def _on_message(self, ws, message):
        received_time = time.time()
        market_data = self._market_data_model.model_validate_json(message)

        for ticker in self.tickers:
            if market_data.symbol.upper() == ticker.symbol_upper:
                ticker.add_data(market_data)

        time_to_receive = received_time - (
            market_data.timestamp / TimeUnits.MILLIS_PER_SECOND.value
        )
        if time_to_receive > 0.5:
            self._logger.warning("Slow message")
        self._logger.info(
            f"{self._exchange.name}-{market_data.symbol} -> ${market_data.close_price}"
            f" || time to receive message: {time_to_receive:.3f}s"
        )

    def stop(self):
        self.stopped = True
        self.ws.close()

    @property
    def tickers(self):
        return self._tickers

    @property
    def thread(self):
        return self._thread
