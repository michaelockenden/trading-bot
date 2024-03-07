from enum import Enum


class Exchanges(Enum):
    GEMINI = "wss://api.gemini.com/v1/marketdata/"
    BINANCE = "wss://stream.binance.com:9443"
