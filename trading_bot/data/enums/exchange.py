from enum import Enum


class Exchange(Enum):
    BINANCE = {
        "websocket": "wss://stream.binance.us:9443",
        "http": "https://api.binance.us",
    }
