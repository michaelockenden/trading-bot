from trading_bot.data.ticker import Ticker
from trading_bot.market_data.binance.BinanceMarketDataProvider import BinanceMarketDataProvider
from trading_bot.client.CryptoClient import CryptoClient
from trading_bot.trading.OrderPlacementManager import OrderPlacementManager


class BinanceClient(CryptoClient):

    def __init__(self):
        tickers = [Ticker("BTCUSDT")]

        super().__init__(OrderPlacementManager(), BinanceMarketDataProvider(tickers))
