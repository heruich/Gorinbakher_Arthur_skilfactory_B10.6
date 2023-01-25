import requests
import json

from config import keys

class ConvertionException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionException(f'невозможно перевести одинаковые валюты {base}')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'не удалось обработать кол-во {amount}')

        # r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        # total_base = json.loads(r.content)[keys[base]]

        base_key = base_ticker
        sym_key = quote_ticker

        url = f"https://api.apilayer.com/exchangerates_data/convert?to={sym_key}&from={base_key}&amount={amount}"

        payload = {}
        headers = {
            "apikey": "YmmyUUo9AsE0Q5gV4jRb0zsPvbLqieLb"
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        # total_base = response.text

        # result = response.text
        r = response.content

        total_base = json.loads(r)["result"]




        return total_base


