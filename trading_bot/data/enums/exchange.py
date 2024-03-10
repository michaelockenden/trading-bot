from enum import Enum


class Exchange(Enum):
    BINANCE = {
        "websocket": "wss://stream.binance.com:9443",
        "http": "https://api.binance.com",
    }
