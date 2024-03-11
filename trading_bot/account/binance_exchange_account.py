from typing import List

from trading_bot.account.exchange_account import ExchangeAccount, ExchangeAPI
from trading_bot.data.enums.exchange import Exchange


class BinanceAPI(ExchangeAPI):

    def __init__(self, api_key: str, api_secret: str):
        super().__init__(api_key, api_secret, Exchange.BINANCE)


class BinanceExchangeAccount(ExchangeAccount):

    def __init__(self, api_key: str, api_secret: str):
        super().__init__(BinanceAPI(api_key, api_secret))

    def get_balance(self):
        endpoint = "/api/v3/account"
        account_info = super().get_account_info(endpoint)
        balances = {}

        for asset in account_info["balances"]:
            asset_name = asset["asset"].upper()
            asset_balance = float(asset["free"])
            if asset_balance > 0:
                balances[asset_name] = asset_balance

        return balances

    def get_account_value_usd(self):
        endpoint = "/api/v1/ticker/price?symbol="
        balances = self.get_balance()
        total_value = 0.0

        for asset, balance in balances.items():
            if asset.upper() == "USDT":
                continue
            price_usd = float(
                self.get_price_info(f"{endpoint}{asset.upper()}USDT")["price"]
            )
            total_value += balance * price_usd

        if "USDT" in [x.upper() for x in balances.keys()]:
            total_value += balances["USDT"]

        return total_value
