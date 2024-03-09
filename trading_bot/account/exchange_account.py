import hashlib
import hmac

import requests
import time


class ExchangeAccount:
    def __init__(self, api_key, api_secret, exchange_name, base_url):
        self.api = ExchangeAPI(api_key, api_secret, exchange_name, base_url)

    def get_account_info(self):
        return self.api.get_account_info()


class ExchangeAPI:
    def __init__(self, api_key, api_secret, exchange_name, base_url):
        self.api_key = api_key
        self.api_secret = api_secret
        self.exchange_name = exchange_name
        self.base_url = base_url

    def _send_signed_request(self, method, endpoint, params=None):
        if params is None:
            params = {}
        timestamp = int(time.time() * 1000)
        params["timestamp"] = timestamp
        params["signature"] = self._generate_signature(params)
        headers = {"X-MBX-APIKEY": self.api_key}
        response = requests.request(
            method, self.base_url + endpoint, params=params, headers=headers
        )
        return response.json()

    def _generate_signature(self, data):
        query_string = "&".join([f"{key}={data[key]}" for key in data])
        return hmac.new(
            self.api_secret.encode(), query_string.encode(), hashlib.sha256
        ).hexdigest()

    def get_account_info(self):
        endpoint = "/api/v3/account"
        return self._send_signed_request("GET", endpoint)


if __name__ == "__main__":
    binance_api_key = None
    binance_api_secret = None
    binance_base_url = "https://api.binance.com"
    binance_account = ExchangeAccount(
        binance_api_key, binance_api_secret, "Binance", binance_base_url
    ).get_account_info()
