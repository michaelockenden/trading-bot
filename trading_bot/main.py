from trading_bot.client.binance.BinanceClient import BinanceClient
from trading_bot.client.gemini.GeminiClient import GeminiClient

if __name__ == "__main__":
    b_client = BinanceClient()
    clients = [b_client]

    for client in clients:
        thread = client.market_data_provider.thread
        if thread is not None:
            thread.join()

