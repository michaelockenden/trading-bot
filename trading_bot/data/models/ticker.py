import time
from collections import deque

from trading_bot.data.models.market_data import MarketData


class Ticker:

    def __init__(self, symbol: str, max_len: int = 1000):
        self._symbol = symbol
        self._data: deque[MarketData] = deque(maxlen=max_len)

    def add_data(self, data_entry: MarketData):
        self._data.append(data_entry)

    def wait_for_data(self, timeout: int):
        count = 0
        while len(self._data) == 0 and count < timeout:
            time.sleep(1)
            count += 1
        if len(self._data) == 0:
            raise RuntimeError("No market data received")

    @property
    def symbol(self):
        return self._symbol.lower()

    @property
    def symbol_upper(self):
        return self._symbol.upper()

    @property
    def market_data_as_list(self):
        return list(self._data)

    @property
    def latest_market_data(self):
        return self._data[-1]
