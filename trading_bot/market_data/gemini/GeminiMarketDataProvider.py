import json
import threading
import time

from trading_bot.data.enums.Exchanges import Exchanges
from trading_bot.data.ticker import Ticker
from trading_bot.market_data.MarketDataProvider import MarketDataProvider


class GeminiMarketDataProvider(MarketDataProvider):

    def __init__(self, tickers: list[Ticker]):
        self._exchange = Exchanges.GEMINI
        super().__init__(tickers, self._exchange)

    def _generate_url(self, tickers: list[Ticker], exchange: Exchanges) -> str:
        if len(tickers) == 1:
            return exchange.value + tickers[0].symbol
        else:
            pass

    def _on_message(self, ws, message):
        increment = json.loads(message)
        event = increment["events"][0]
        price = event["price"]
        symbol = self.tickers[0].symbol_upper
        print(f"{self._exchange.name}-{symbol} -> {price}")
        time.sleep(0.5)
