import time

from trading_bot.data.enums.exchange import Exchange
from trading_bot.data.enums.interval import Interval
from trading_bot.data.enums.time_units import TimeUnits
from trading_bot.data.models.market_data import (
    BinanceMarketData,
)
from trading_bot.data.models.ticker import Ticker
from trading_bot.market_data.market_data_provider import MarketDataProvider
from trading_bot.utils.logging import TradingBotLogger


class BinanceMarketDataProvider(MarketDataProvider):

    def __init__(self, tickers: list[Ticker], interval: Interval):
        self._exchange = Exchange.BINANCE
        super().__init__(tickers, self._exchange, interval)
        self._logger = TradingBotLogger("BinanceMarketDataProvider").get_logger()

    def _generate_url(
        self, tickers: list[Ticker], exchange: Exchange, interval: Interval
    ) -> str:
        if len(tickers) == 1:
            return exchange.value + f"/ws/{tickers[0].symbol}@kline_{interval.value}"
        else:
            stream_names = []
            for ticker in tickers:
                stream_names.append(f"{ticker.symbol}@kline_{interval.value}")
            stream_names = "/".join(stream_names)
            return exchange.value + f"/stream?streams={stream_names}"

    def _on_message(self, ws, message):
        received_time = time.time()
        market_data = BinanceMarketData.model_validate_json(message)

        for ticker in self.tickers:
            if market_data.symbol == ticker.symbol_upper:
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
