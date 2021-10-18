import locale
import platform
from datetime import datetime

from bs4 import BeautifulSoup

from webapp.news.parsers.utils import get_html, seve_news

if platform.system() == "Windows":
    locale.setlocale(locale.LC_ALL, "russian")
else:
    locale.setlocale(locale.LC_TIME, "ru_RU.UTF-8")


def parse_habr_date(date_str):
    today = datetime.now()
    date_str = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.000Z")
    try:
        return date_str.strftime("%d %B %Y в %H:%M")
    except ValueError:
        return today.strftime("%d %B %Y")


def get_habr_snippets():
    for page_count in range(50):
        html = get_html(f"https://habr.com/ru/hub/python/page{page_count}/")
        if html:
            soup = BeautifulSoup(html, "html.parser")
            all_news = soup.find("div", class_="tm-articles-list").find_all(
                "article", class_="tm-articles-list__item"
            )
            for new in all_news:
                title = (
                    new.find("a", class_="tm-article-snippet__title-link")
                    .find("span")
                    .text
                )
                url = new.find("a", class_="tm-article-snippet__title-link")["href"]
                url = f"https://habr.com{url}"
                published = new.find(
                    "span", class_="tm-article-snippet__datetime-published"
                ).find("time")["datetime"]
                published = parse_habr_date(published)
                # print(published + '\n' + title + '\n' + url + '\n')
                seve_news(title, url, published)
