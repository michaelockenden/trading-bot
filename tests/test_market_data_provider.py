from unittest import TestCase, skip

from trading_bot.data.enums.interval import Interval
from trading_bot.data.models.ticker import Ticker
from trading_bot.market_data.binance_market_data_provider import (
    BinanceMarketDataProvider,
)
from trading_bot.market_data.market_data_provider import MarketDataProvider


class TestMarketDataProvider(TestCase):

    def __init__(self, methodName="runTest"):
        super().__init__(methodName)
        self._provider: MarketDataProvider
        self._symbol = "BTCUSDT"

    def setUp(self):
        self._provider = BinanceMarketDataProvider(
            [Ticker(self._symbol)], Interval.ONE_MINUTE
        )
        self._provider.wait_for_connection(30)
        self._provider.get_ticker(self._symbol).wait_for_data(30)

    def tearDown(self):
        self._provider.stop()

@skip("API Test Skipped")
    def test_market_data_provider_receives_data_from_external_stream(self):
        md = self._provider.get_ticker(self._symbol).latest_market_data

        self.assertIsInstance(md.close_price, str)
        self.assertIsInstance(md.symbol, str)
        self.assertIsInstance(md.timestamp, int)
