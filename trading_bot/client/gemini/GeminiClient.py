from trading_bot.client.CryptoClient import CryptoClient
from trading_bot.data.ticker import Ticker
from trading_bot.market_data.gemini.GeminiMarketDataProvider import GeminiMarketDataProvider
from trading_bot.trading.OrderPlacementManager import OrderPlacementManager


class GeminiClient(CryptoClient):

    def __init__(self):
        tickers = [Ticker("BTCUSDT")]

        super().__init__(OrderPlacementManager(), GeminiMarketDataProvider(tickers))
