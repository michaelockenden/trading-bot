from typing import Type

from trading_bot.data.models.market_data import MarketData
from trading_bot.market_data.websocket_client import WebsocketClient


class TestWebsocketClient(WebsocketClient):

    def __init__(self, market_data_model: Type[MarketData]):
        super().__init__("ws://127.0.0.1:5000")
        self._market_data_model = market_data_model

    def _on_message(self, ws, message):
        super().logger.info(self._market_data_model.model_validate_json(message))
