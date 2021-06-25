from datetime import datetime

import requests
from bs4 import BeautifulSoup


from webapp.db import db
from webapp.news.models import News


def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except (requests.RequestException, ValueError):
        print("Сетевая ошибка")
        return False


def get_python_news():
    html = get_html("https://www.python.org/blogs/")
    if html:
        soup = BeautifulSoup(html, "html.parser")
        all_news = soup.find("ul", class_="list-recent-posts").findAll("li")
        result_news = []
        for new in all_news:
            title = new.find("a").text
            url = new.find("a")["href"]
            published = new.find("time").text
            try:
                published = datetime.strptime(published, "%Y-%m-%d")
            except (ValueError):
                published = datetime.now()
            seve_news(title, url, published)


def seve_news(title, url, published):
    news_exists = News.query.filter(News.url == url).count()
    print(news_exists)
    if not news_exists:
        news_news = News(title=title, url=url, published=published)
        db.session.add(news_news)
        db.session.commit()
