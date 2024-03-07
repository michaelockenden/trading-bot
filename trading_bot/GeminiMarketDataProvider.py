import json
import threading
import time

from trading_bot.Exchanges import Exchanges
from trading_bot.MarketDataProvider import MarketDataProvider


class GeminiMarketDataProvider(MarketDataProvider):

    def __init__(self, tickers: tuple[str, ...]):
        self._exchange = Exchanges.GEMINI
        super().__init__(tickers, self._exchange)

    def get_thread(self) -> threading.Thread:
        return super().get_thread()

    def get_tickers(self) -> tuple[str, ...]:
        return super().get_tickers()

    def _generate_url(self, tickers: tuple[str, ...], exchange: Exchanges) -> str:
        if len(tickers) == 1:
            return exchange.value + tickers[0].upper()
        else:
            pass

    def _on_message(self, ws, message):
        increment = json.loads(message)
        event = increment["events"][0]
        price = event["price"]
        symbol = self.get_tickers()[0]
        print(f"{self._exchange.name}-{symbol} -> {price}")
        time.sleep(0.5)

