import time

from flask import Flask, render_template
from flask_socketio import SocketIO
import threading
import csv


class BacktestingEnvironment:
    def __init__(self, csv_file: str):
        self.app = Flask(__name__)
        self.socketio = SocketIO(self.app)
        self.csv_file = csv_file

        @self.app.route("/")
        def index() -> str:
            return render_template("index.html")

        @self.socketio.on("connect")
        def handle_connect() -> None:
            threading.Thread(target=self.stream_data).start()

    def stream_data(self) -> None:
        with open(self.csv_file, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                timestamp = row[0]
                data = {"timestamp": timestamp, "price": float(row[4])}
                self.socketio.emit("data", data)
                time.sleep(1)

    def run(self, host: str = "localhost", port: int = 5000) -> None:
        self.socketio.run(
            self.app,
            host=host,
            port=port,
            use_reloader=False,
            log_output=False,
            allow_unsafe_werkzeug=True,
        )
