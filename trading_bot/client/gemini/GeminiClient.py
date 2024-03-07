from trading_bot.client.CryptoClient import CryptoClient
from trading_bot.market_data.gemini.GeminiMarketDataProvider import GeminiMarketDataProvider
from trading_bot.trading.OrderPlacementManager import OrderPlacementManager


class GeminiClient(CryptoClient):

    def __init__(self):
        tickers = ("BTCUSD",)
        super().__init__(OrderPlacementManager(), GeminiMarketDataProvider(tickers))

    def get_market_data_provider(self) -> GeminiMarketDataProvider:
        return super().get_market_data_provider()

    def get_order_placement_manager(self) -> OrderPlacementManager:
        return super().get_order_placement_manager()

