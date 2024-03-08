import json
import time

from trading_bot.data.enums.exchanges import Exchanges
from trading_bot.data.ticker import Ticker
from trading_bot.market_data.market_data_provider import MarketDataProvider


class BinanceMarketDataProvider(MarketDataProvider):

    def __init__(self, tickers: list[Ticker]):
        self._exchange = Exchanges.BINANCE
        super().__init__(tickers, self._exchange)

    def _generate_url(self, tickers: list[Ticker], exchange: Exchanges) -> str:
        if len(tickers) == 1:
            return exchange.value + f"/ws/{tickers[0].symbol}@kline_1m"
        else:
            stream_names = []
            for ticker in tickers:
                stream_names.append(f"{ticker.symbol}@kline_1m")
            stream_names = "/".join(stream_names)
            return exchange.value + f"/stream?streams={stream_names}"

    def _on_message(self, ws, message):
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

        time_to_handle = time.time() - (int(timestamp) / 1000)
        if time_to_handle > 0.5:
            print("Slow message")
        print(
            f"{self._exchange.name}-{symbol} -> ${price.rstrip('0').rstrip('.')}"
            f" || time to receive message: {time_to_handle:.3f}s"
        )
