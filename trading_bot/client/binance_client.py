from trading_bot.data.enums.interval import Interval
from trading_bot.data.models.ticker import Ticker
from trading_bot.market_data.binance_market_data_provider import (
    BinanceMarketDataProvider,
)
from trading_bot.client.crypto_client import CryptoClient
from trading_bot.trading.order_placement_manager import OrderPlacementManager


class BinanceClient(CryptoClient):

    def __init__(self, tickers: list[Ticker], interval: Interval):
        super().__init__(
            OrderPlacementManager(), BinanceMarketDataProvider(tickers, interval)
        )