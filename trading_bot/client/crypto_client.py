from trading_bot.trading import order_placement_manager
from trading_bot.market_data import market_data_provider


class CryptoClient:

    def __init__(self, order_placement_manager: OrderPlacementManager, market_data_provider: MarketDataProvider):
        self._market_data_provider = market_data_provider
        self._order_placement_manager = order_placement_manager

    @property
    def market_data_provider(self):
        return self._market_data_provider

    @property
    def order_placement_manager(self):
        return self._order_placement_manager
