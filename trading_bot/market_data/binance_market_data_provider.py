from trading_bot.data.enums.exchange import Exchange
from trading_bot.data.enums.interval import Interval
from trading_bot.data.models.market_data import (
    BinanceMarketData,
)
from trading_bot.data.models.ticker import Ticker
from trading_bot.market_data.market_data_provider import MarketDataProvider
from trading_bot.utils.logging import TradingBotLogger


class BinanceMarketDataProvider(MarketDataProvider):

    def __init__(self, tickers: list[Ticker], interval: Interval):
        super().__init__(tickers, Exchange.BINANCE, interval, BinanceMarketData)
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
