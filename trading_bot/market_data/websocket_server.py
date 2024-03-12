import asyncio
import csv

import websockets  # type: ignore

from trading_bot.data.enums.exchange import Exchange
from trading_bot.data.models.market_data import MarketData, get_json_from_base_model


class WebsocketServer:

    def __init__(self, csv_file, exchange: Exchange):
        self._csv_file = csv_file
        self._exchange = exchange
        self._server = websockets.serve(self.stream_data, "localhost", 5000)
        self._event_loop = asyncio.get_event_loop()
        self._event_loop.run_until_complete(self._server)
        self._event_loop.run_forever()

    async def stream_data(self, websocket, path):
        with open(self._csv_file, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                data = {
                    "symbol": row[0],
                    "timestamp": row[1],
                    "close_price": row[2],
                    "quote_volume": row[3],
                    "candle_close": row[4],
                    "interval": row[5],
                }

                data = MarketData(**data)
                await websocket.send(get_json_from_base_model(self._exchange, data))
