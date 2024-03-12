import json

from pydantic import BaseModel, Field, AliasPath, AliasChoices

from trading_bot.data.enums.exchange import Exchange
from trading_bot.data.enums.interval import Interval


class MarketData(BaseModel):
    symbol: str
    timestamp: int
    close_price: str
    quote_volume: str
    candle_close: bool
    interval: Interval


def get_binance_json_from_base_model(market_data_obj: MarketData):
    binance_market_data_json = market_data_obj.dict()
    binance_market_data_json["data"] = {
        "s": binance_market_data_json.pop("symbol"),
        "E": binance_market_data_json.pop("timestamp"),
        "k": {
            "c": binance_market_data_json.pop("close_price"),
            "q": binance_market_data_json.pop("quote_volume"),
            "x": binance_market_data_json.pop("candle_close"),
            "i": binance_market_data_json.pop("interval").value,
        },
    }

    return json.dumps(binance_market_data_json)


def get_json_from_base_model(exchange: Exchange, market_data_obj: MarketData):
    if exchange == Exchange.BINANCE:
        return get_binance_json_from_base_model(market_data_obj)


class BinanceMarketData(MarketData):
    symbol: str = Field(validation_alias=AliasChoices("s", AliasPath("data", "s")))
    timestamp: int = Field(validation_alias=AliasChoices("E", AliasPath("data", "E")))
    close_price: str = Field(
        validation_alias=AliasChoices(AliasPath("k", "c"), AliasPath("data", "k", "c"))
    )
    quote_volume: str = Field(
        validation_alias=AliasChoices(AliasPath("k", "q"), AliasPath("data", "k", "q"))
    )
    candle_close: bool = Field(
        validation_alias=AliasChoices(AliasPath("k", "x"), AliasPath("data", "k", "x"))
    )
    interval: Interval = Field(
        validation_alias=AliasChoices(AliasPath("k", "i"), AliasPath("data", "k", "i"))
    )
