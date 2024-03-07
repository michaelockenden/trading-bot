from trading_bot.trading import OrderPlacementManager
from trading_bot.market_data import MarketDataProvider


class CryptoClient:

    def __init__(self, order_placement_manager: OrderPlacementManager, market_data_provider: MarketDataProvider):
        self._market_data_provider = market_data_provider
        self._order_placement_manager = order_placement_manager

    def get_market_data_provider(self) -> MarketDataProvider:
        return self._market_data_provider

    def get_order_placement_manager(self) -> OrderPlacementManager:
        return self._order_placement_manager
