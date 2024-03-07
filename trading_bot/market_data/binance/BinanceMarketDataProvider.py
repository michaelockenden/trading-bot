import json
import threading

from trading_bot.data.enums.Exchanges import Exchanges
from trading_bot.market_data.MarketDataProvider import MarketDataProvider


class BinanceMarketDataProvider(MarketDataProvider):

    def __init__(self, tickers: tuple[str, ...]):
        self._exchange = Exchanges.BINANCE
        super().__init__(tickers, self._exchange)

    def get_thread(self) -> threading.Thread:
        return super().get_thread()

    def get_tickers(self) -> tuple[str, ...]:
        return super().get_tickers()

    def _generate_url(self, tickers: tuple[str, ...], exchange: Exchanges) -> str:
        if len(tickers) == 1:
            return exchange.value + f"/ws/{tickers[0].lower()}@kline_1m"
        else:
            stream_names = []
            for ticker in tickers:
                stream_names.append(f"{ticker.lower()}@kline_1m")
            stream_names = "/".join(stream_names)
            return exchange.value + f"/stream?streams={stream_names}"

    def _on_message(self, ws, message):
        increment = json.loads(message)
        candle = increment["k"]
        price = candle["c"]
        symbol = candle["s"]
        print(f"{self._exchange.name}-{symbol} -> {price}")

