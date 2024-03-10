from trading_bot.account.exchange_account import ExchangeAccount
from trading_bot.data.enums.interval import Interval
from trading_bot.client.binance_client import BinanceClient
from trading_bot.data.models.ticker import Ticker
from trading_bot.data.enums.exchange import Exchange
from trading_bot.market_data.binance_market_data_provider import BinanceMarketDataProvider
from trading_bot.market_data.market_data_provider import MarketDataProvider


class BinanceExchangeAccount(ExchangeAccount):

    def __init__(self, api_key: str, api_secret: str):
        super().__init__(api_key, api_secret, Exchange.BINANCE)
        self.market_data_provider = None

    def get_balance(self):
        account_info = super().get_account_info()

        balances = {}
        for asset in account_info["balances"]:
            asset_name = asset["asset"]
            asset_balance = float(asset["free"])
            if asset_balance > 0:
                balances[asset_name] = asset_balance

        return balances

    def get_account_value_usd(self):
        balances = self.get_balance()
        total_value = 0.0
        prices = {}

        if self.market_data_provider is None:
            tickers = [Ticker(asset.upper() + "USDT") for asset in balances.keys() if
                       asset.upper() not in ('USDT', 'GBP')]
            self.market_data_provider = BinanceMarketDataProvider(tickers, Interval.ONE_MINUTE)

        for ticker in self.market_data_provider.tickers:
            print(ticker.symbol)
            ticker.wait_for_data(30)
            ticker_price = float(ticker.latest_market_data.close_price)
            symbol = ticker.latest_market_data.symbol.upper()
            prices[symbol] = ticker_price

        for asset, balance in balances.items():
            if asset.upper() + "USDT" in prices:
                price_usd = prices[asset.upper() + "USDT"]
                total_value += balance * price_usd

        if 'USDT' in balances:
            total_value += balances['USDT']

        return total_value

