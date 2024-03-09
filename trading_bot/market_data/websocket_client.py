import time

import websocket


class WebsocketClient:

    def __init__(self, url: str):
        self._ws = self._init_socket(url)
        self._stopped = True

    @property
    def ws(self):
        return self._ws

    @property
    def stopped(self):
        return self._stopped

    @stopped.setter
    def stopped(self, value):
        self._stopped = value

    def _on_message(self, ws, message):
        print(message)

    def _on_error(self, ws, error):
        print(error)

    def _on_close(self, ws, close_status_code, close_msg):
        print("### closed ###")

    def _on_open(self, ws):
        print("Opened connection")

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
        while not self._stopped:
            self._ws.run_forever()
            time.sleep(5)
