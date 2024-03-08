from trading_bot.market_data.binance.BinanceMarketDataProvider import BinanceMarketDataProvider
from trading_bot.client.CryptoClient import CryptoClient
from trading_bot.trading.OrderPlacementManager import OrderPlacementManager


class BinanceClient(CryptoClient):

    def __init__(self):
        tickers = ("btcusdt", "ethusdt", "solusdt")
        super().__init__(OrderPlacementManager(), BinanceMarketDataProvider(tickers))

    def get_market_data_provider(self) -> BinanceMarketDataProvider:
        return super().get_market_data_provider()

    def get_order_placement_manager(self) -> OrderPlacementManager:
        return super().get_order_placement_manager()
