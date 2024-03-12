from trading_bot.data.enums.exchange import Exchange
from trading_bot.market_data.websocket_server import WebsocketServer


class BinanceMarketDataServer(WebsocketServer):

    def __init__(self, csv_file):
        super().__init__(csv_file, Exchange.BINANCE)
