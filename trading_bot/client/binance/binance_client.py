from trading_bot.data.enums.intervals import Intervals
from trading_bot.data.ticker import Ticker
from trading_bot.market_data.binance.binance_market_data_provider import (
    BinanceMarketDataProvider,
)
from trading_bot.client.crypto_client import CryptoClient
from trading_bot.trading.order_placement_manager import OrderPlacementManager


class BinanceClient(CryptoClient):

    def __init__(self, tickers: list[Ticker], interval: Intervals):
        super().__init__(
            OrderPlacementManager(), BinanceMarketDataProvider(tickers, interval)
        )
