import requests
from bs4 import BeautifulSoup


class Parsers:
    html = ""
    res = []

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        req = requests.get(self.url).text
        self.html = BeautifulSoup(req, 'lxml')

    def parsing(self):
        news = self.html.find_all("div", class_="caption")
        for item in news:
            title = item.find('h3').text
            href = item.find('a').get('href')
            author = item.find('a', class_='topic-info-author-link').text.strip()
            self.res.append({
                "title": title,
                "href": href,
                "author": author
            })
        # print(self.res)

    def save(self):
        with open(self.path, 'w') as f:
            i = 1
            for item in self.res:
                f.write(f"Новость № {i}\n\nНазвание: {item['title']}\nСсылка: {item['href']}\nАвтор: {item['author']}"
                        f"\n\n{'*' * 20}\n")
                i += 1

    def run(self):
        self.get_html()
        self.parsing()
        self.save()
