from trading_bot import OrderPlacementManager, MarketDataProvider


class CryptoClient:

    def __init__(self, order_placement_manager: OrderPlacementManager, market_data_provider: MarketDataProvider):

        self.market_data_provider = market_data_provider
        self.order_placement_manager = order_placement_manager

