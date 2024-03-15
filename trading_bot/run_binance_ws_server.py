from trading_bot.market_data.binance_market_data_server import BinanceMarketDataServer
from trading_bot.utils.file_utils import project_root


def main():
    BinanceMarketDataServer(project_root() / "trading_bot/market_data/csv.csv")


if __name__ == "__main__":
    main()
