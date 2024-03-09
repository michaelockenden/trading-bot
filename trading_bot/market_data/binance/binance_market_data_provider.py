import json
import time

from trading_bot.data.enums.exchange import Exchange
from trading_bot.data.enums.interval import Interval
from trading_bot.data.enums.time_units import TimeUnits
from trading_bot.data.ticker import Ticker
from trading_bot.market_data.market_data_provider import MarketDataProvider
from trading_bot.utils.num_utils import remove_trailing_zeroes


class BinanceMarketDataProvider(MarketDataProvider):

    def __init__(self, tickers: list[Ticker], interval: Interval):
        self._exchange = Exchange.BINANCE
        super().__init__(tickers, self._exchange, interval)

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
        increment = json.loads(message)
        if len(self.tickers) == 1:
            timestamp = increment["E"]
            candle = increment["k"]
            price = candle["c"]
            symbol = candle["s"]
        else:
            increment = increment["data"]
            timestamp = increment["E"]
            candle = increment["k"]
            price = candle["c"]
            symbol = candle["s"]

        for ticker in self.tickers:
            if symbol == ticker.symbol_upper:
                ticker.add_data(increment)

        time_to_receive = received_time - (
            int(timestamp) / TimeUnits.MILLIS_PER_SECOND.value
        )
        if time_to_receive > 0.5:
            print("Slow message")
        print(
            f"{self._exchange.name}-{symbol} -> ${remove_trailing_zeroes(price)}"
            f" || time to receive message: {time_to_receive:.3f}s"
        )
