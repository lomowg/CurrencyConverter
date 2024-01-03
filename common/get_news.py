import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def get_articles():
    articles = []

    url = "https://ria.ru/economy/"
    response = requests.get(url)
    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')

    article_divs = soup.find_all('div', class_='list-item__content')

    for article_div in article_divs:
        article_link = article_div.find('a', class_='list-item__title')['href']
        full_article_link = urljoin(url, article_link)

        article_title = article_div.find('a', class_='list-item__title').text

        image_url = article_div.find('img')['src']

        full_image_url = urljoin(url, image_url)

        articles.append({'title': article_title, 'url': full_article_link, 'image': full_image_url, 'time': 0})

    article_divs = soup.find_all('div', class_='list-item__info')

    for i in range(len(article_divs)):
        article_time = article_divs[i].find('div', class_='list-item__date').text
        articles[i]['time'] = article_time

    return articles
