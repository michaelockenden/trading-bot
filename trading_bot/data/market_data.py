from datetime import datetime

from pydantic import BaseModel, Field, AliasPath


class MarketData(BaseModel):
    symbol: str
    timestamp: datetime
    close_price: float
    quote_volume: float
    candle_close: bool
    interval: str  # TODO: change to enum


class BinanceMarketData(MarketData):
    symbol: str = Field(validation_alias="s")
    timestamp: datetime = Field(validation_alias="E")
    close_price: float = Field(validation_alias=AliasPath("k", "c"))
    quote_volume: float = Field(validation_alias=AliasPath("k", "q"))
    candle_close: bool = Field(validation_alias=AliasPath("k", "x"))
    interval: str = Field(validation_alias=AliasPath("k", "i"))


class BinanceNestedMarketData(MarketData):
    symbol: str = Field(validation_alias=AliasPath("data", "s"))
    timestamp: datetime = Field(validation_alias=AliasPath("data", "E"))
    close_price: float = Field(validation_alias=AliasPath("data", "k", "c"))
    quote_volume: float = Field(validation_alias=AliasPath("data", "k", "q"))
    candle_close: bool = Field(validation_alias=AliasPath("data", "k", "x"))
    interval: str = Field(validation_alias=AliasPath("data", "k", "i"))