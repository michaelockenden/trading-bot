import hashlib
import hmac

import requests
import time

from trading_bot.data.enums.exchange import Exchange
from trading_bot.data.enums.time_units import TimeUnits


class ExchangeAccount:
    def __init__(self, api_key: str, api_secret: str, exchange: Exchange):
        self._api = ExchangeAPI(api_key, api_secret, exchange)

    def get_account_info(self):
        return self._api.get_account_info()


class ExchangeAPI:
    def __init__(self, api_key: str, api_secret: str, exchange: Exchange):
        self._api_key = api_key
        self._api_secret = api_secret
        self._base_url = exchange.value["http"]

    def send_signed_request(self, method, endpoint, params=None):
        if params is None:
            params = {}
        timestamp = int(time.time() * TimeUnits.MILLIS_PER_SECOND.value)
        params["timestamp"] = timestamp
        params["signature"] = self._generate_signature(params)
        headers = {"X-MBX-APIKEY": self._api_key}
        response = requests.request(
            method, self._base_url + endpoint, params=params, headers=headers
        )
        return response.json()

    def _generate_signature(self, data):
        query_string = "&".join([f"{key}={data[key]}" for key in data])
        return hmac.new(
            self._api_secret.encode(), query_string.encode(), hashlib.sha256
        ).hexdigest()

    def get_account_info(self):
        endpoint = "/api/v3/account"
        return self.send_signed_request("GET", endpoint)
