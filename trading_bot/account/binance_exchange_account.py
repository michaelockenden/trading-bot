from trading_bot.account.exchange_account import ExchangeAccount
from trading_bot.data.enums.interval import Interval
from trading_bot.client.binance_client import BinanceClient


class BinanceExchangeAccount(ExchangeAccount):
    BASE_URL = "https://api.binance.com"

    def __init__(self, api_key, api_secret):
        super().__init__(api_key, api_secret, "Binance", self.BASE_URL)

    def get_balance(self):
        endpoint = "/api/v3/account"
        account_info = self.api.send_signed_request("GET", endpoint)

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
        prices = []  # TODO

        for asset, balance in balances.items():
            if asset in prices:
                price_usd = prices[asset]
                total_value += balance * price_usd

        return total_value


if __name__ == "__main__":
    API_KEY = ""
    API_SECRET = ""

    binance_account = BinanceExchangeAccount(API_KEY, API_SECRET)
    balance = binance_account.get_account_value_usd()
    print(balance)
