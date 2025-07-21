import time
import websocket  # type: ignore
from trading_bot.utils.logging import TradingBotLogger


class WebsocketClient:

    def __init__(self, url: str):
        self._ws = self._init_socket(url)
        self._stopped = True
        self._connected = False
        self._logger = TradingBotLogger("WebsocketClient").get_logger()

    @property
    def ws(self):
        return self._ws

    @property
    def stopped(self):
        return self._stopped

    @stopped.setter
    def stopped(self, value: bool):
        self._stopped = value

    @property
    def logger(self):
        return self._logger

    def wait_for_connection(self, timeout: int):
        count = 0
        while not self._connected and count < timeout:
            time.sleep(1)
            count += 1
        if not self._connected:
            raise ConnectionError("Connection timed out")

    def _on_message(self, ws, message):
        self._logger.info(message)

    def _on_error(self, ws, error):
        self._logger.error(error)

    def _on_close(self, ws, close_status_code, close_msg):
        self._connected = False
        self._logger.info(f"Closed connection: {close_status_code=}, {close_msg=}")
        if int(close_status_code) == 1000 and close_msg == "":
            self._stopped = True

    def _on_open(self, ws):
        self._connected = True
        self._logger.info("Opened connection")

    def _init_socket(self, url) -> websocket.WebSocketApp:
        return websocket.WebSocketApp(
            url=url,
            on_open=self._on_open,
            on_error=self._on_error,
            on_close=self._on_close,
            on_message=self._on_message,
        )

    def run(self):
        self._stopped = False
        while not self._stopped and not self._connected:
            self._ws.run_forever()
            time.sleep(5)
