def get_interest_rate(start_day, end_day=None):
    import requests
    from bs4 import BeautifulSoup
    from datetime import datetime

    if end_day is None:
        end_day = start_day

    response = requests.get(f'https://cbr.ru/hd_base/KeyRate/?UniDbQuery.Posted=True&UniDbQuery.From={start_day}&UniDbQuery.To={end_day}')

    while response.status_code != 200:
        response = requests.get(f'https://cbr.ru/hd_base/KeyRate/?UniDbQuery.Posted=True&UniDbQuery.From={start_day}&UniDbQuery.To={end_day}')

    soup = BeautifulSoup(response.text, 'lxml')

    tbody_tag = soup.find('table')

    rows = tbody_tag.find_all('tr')

    result = []
    for row in rows:
        cells = row.find_all('td')
        element = tuple(i.text for i in cells)
        if element:
            result.append((datetime.strptime(element[0], '%d.%m.%Y'), float(element[1].replace(',', '.'))))

    return result