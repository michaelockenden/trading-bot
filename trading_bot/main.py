from trading_bot.BinanceClient import BinanceClient
from trading_bot.GeminiClient import GeminiClient

if __name__ == "__main__":
    b_client = BinanceClient()
    g_client = GeminiClient()
    clients = [b_client, g_client]

    for client in clients:
        thread = client.get_market_data_provider().get_thread()
        if thread is not None:
            thread.join()

