from trading_bot.Exchanges import Exchanges
from trading_bot.WebsocketClient import WebsocketClient


class MarketDataProvider(WebsocketClient):

    def __init__(self, tickers: tuple[str, ...], exchange: Exchanges):
        super().__init__(self._generate_url(tickers, exchange))
        super().run()

    def _generate_url(self, tickers: tuple[str, ...], exchange: Exchanges) -> str:
        pass

    def _on_message(self, ws, message):
        print(f"{message=}")

