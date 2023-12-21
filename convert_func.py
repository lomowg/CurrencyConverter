def convert(input_cur, output_cur, amount, reverse=False):
    from pycbrf import ExchangeRates
    from datetime import datetime

    date_now = datetime.now().date().isoformat()
    rates = ExchangeRates(date_now, locale_en=True)

    if isinstance(amount, str) or amount is None:
        return 0

    if input_cur == output_cur:
        multiplier_1 = 1
        multiplier_2 = 1
    elif input_cur == 'RUB':
        multiplier_1 = rates[output_cur].rate
        multiplier_2 = 1/rates[output_cur].rate
    elif output_cur == 'RUB':
        multiplier_1 = 1/rates[input_cur].rate
        multiplier_2 = rates[input_cur].rate
    else:
        multiplier_1 = rates[input_cur].rate/rates[output_cur].rate
        multiplier_2 = 1/multiplier_1

    return amount*float(multiplier_2) if reverse else amount*float(multiplier_1)
