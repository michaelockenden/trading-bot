from trading_bot.Exchanges import Exchanges
from trading_bot.MarketDataProvider import MarketDataProvider


class BinanceMarketDataProvider(MarketDataProvider):

    def __init__(self, tickers: tuple[str, ...]):
        self._exchange = Exchanges.BINANCE
        super().__init__(tickers, self._exchange)

    def _generate_url(self, tickers: tuple[str, ...], exchange: Exchanges) -> str:
        if len(tickers) == 1:
            return exchange.value + f"/ws/{tickers[0].lower()}@kline_1m"
        else:
            stream_names = []
            for ticker in tickers:
                stream_names.append(f"{ticker.lower()}@kline_1m")
            stream_names = "/".join(stream_names)
            return exchange.value + f"/stream?streams={stream_names}"

