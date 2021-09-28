from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import locale
import platform
import time

from webapp.news.parsers.utils import get_html, seve_news


if platform.system() == "Windows":
    locale.setlocale(locale.LC_ALL, "russian")
else:
    locale.setlocale(locale.LC_TIME, "ru_RU.UTF-8")


def parse_habr_date(date_str):
    today = datetime.now()
    if "сегодня" in date_str:
        date_str = date_str.replace("сегодня", today.strftime("%d %B %Y"))
    elif "вчера" in date_str:
        yesterday = datetime.now() - timedelta(days=1)
        date_str = date_str.replace("вчера", yesterday.strftime("%d %B %Y"))
    try:
        return datetime.strptime(date_str, "%d %B %Y в %H:%M")
    except ValueError:
        return today.strftime("%d %B %Y")


def get_habr_snippets():
    for page_count in range(50):
        html = get_html(f"https://habr.com/ru/hub/python/page{page_count}/")
        # html = get_html("https://habr.com/ru/search/?q=Python&target_type=posts&order=relevance")
        if html:
            soup = BeautifulSoup(html, "html.parser")
            all_news = soup.find("div", class_="tm-articles-list").find_all("article", class_="tm-articles-list__item")
            for new in all_news:
                title = new.find("a", class_="tm-article-snippet__title-link").find("span").text
                url = new.find("a", class_="tm-article-snippet__title-link")["href"]
#               published = new.find("span", class_="tm-article-snippet__datetime-published").find("time").text
                published = new.find("span", class_="tm-article-snippet__datetime-published").find("time")["datetime"]
                print(published + '\n' + title + '\n' + url + '\n')
#               published = parse_habr_date(published)
#               seve_news(title, url, published)
