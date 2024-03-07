from trading_bot.BinanceMarketDataProvider import BinanceMarketDataProvider
from trading_bot.CryptoClient import CryptoClient
from trading_bot.OrderPlacementManager import OrderPlacementManager


class BinanceClient(CryptoClient):

    def __init__(self):
        tickers = ("btcusdt", "ethusdt", "solusdt")
        super().__init__(OrderPlacementManager(), BinanceMarketDataProvider(tickers))
