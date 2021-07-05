from decouple import config
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


class Near:
    def __init__(self):
        self.crypto_symbol = 'NEAR'
        self.currency = config('CURRENCY_TO_CONVERT')

    def getData(self):
        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
        parameters = {
            'convert': self.currency,
            'symbol': self.crypto_symbol
        }
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': config('CMC_API_KEY'),
        }

        session = Session()
        session.headers.update(headers)

        try:
            response = session.get(url, params=parameters)
            data = json.loads(response.text)
            if data['status']['error_code'] != 0:
                print('erro', data['status'])
            else:
                return {
                    'price': data['data'][self.crypto_symbol]['quote'][self.currency]['price'],
                    'percent_change_24h': data['data'][self.crypto_symbol]['quote'][self.currency]['percent_change_24h']
                }
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            raise Exception('Error while trying to get the price and percentage: ' + e.reason)
