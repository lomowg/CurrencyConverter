from pycbrf import ExchangeRates
from datetime import datetime

date_now = datetime.now().date().isoformat()
rates = ExchangeRates(date_now, locale_en=True)
common_codes = ['RUB', 'USD', 'EUR']

CODES = common_codes + sorted([i.code for i in rates.rates if i.code not in common_codes])
