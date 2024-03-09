from pydantic import BaseModel, Field, AliasPath, AliasChoices

from trading_bot.data.enums.interval import Interval


class MarketData(BaseModel):
    symbol: str
    timestamp: int
    close_price: float
    quote_volume: float
    candle_close: bool
    interval: Interval


class BinanceMarketData(MarketData):
    symbol: str = Field(validation_alias=AliasChoices("s", AliasPath("data", "s")))
    timestamp: int = Field(validation_alias=AliasChoices("E", AliasPath("data", "E")))
    close_price: float = Field(
        validation_alias=AliasChoices(AliasPath("k", "c"), AliasPath("data", "k", "c"))
    )
    quote_volume: float = Field(
        validation_alias=AliasChoices(AliasPath("k", "q"), AliasPath("data", "k", "q"))
    )
    candle_close: bool = Field(
        validation_alias=AliasChoices(AliasPath("k", "x"), AliasPath("data", "k", "x"))
    )
    interval: Interval = Field(
        validation_alias=AliasChoices(AliasPath("k", "i"), AliasPath("data", "k", "i"))
    )
