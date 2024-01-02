import yfinance as yf
import pandas as pd


def get_imoex_index(start_day, end_day):
    imoex = yf.Ticker("IMOEX.ME")
    data = pd.DataFrame(imoex.history(start=start_day, end=end_day, interval="1d")['Close']).reset_index().sort_values('Date', ascending=False)
    data['Close'] = round(data['Close'], 2)
    data.columns = ['Дата', 'Значение']

    return data


