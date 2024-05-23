"""
Парсинг https://quotes.toscrape.com
По мотивам https://www.geeksforgeeks.org/quote-guessing-game-using-web-scraping-in-python/
"""
from bs4 import BeautifulSoup
import requests
from rich.console import Console
from dataclasses import dataclass, asdict
import json


@dataclass
class Quote:
    text: str
    author: str
    keywords: list[str]
    autor_url: str

parsed = {}
console = Console()

base_url = 'https://quotes.toscrape.com'
FILE_TO_SAVE = 'quotes.json'
page = 0
id = 1

ref_next = True
while ref_next:
    page += 1
    if page > 1:
        url = f"{base_url}{ref_next[0].attrs['href']}"
    else:
        url = base_url
    # print(f'Страница {page}: {url}')
    style = "bold white on blue"
    console.rule(f"[{style}]{page}")
    with console.status(f'Страница {page}: {url}', spinner='arrow', spinner_style=style):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')  # лучше и быстрее lxml, нужно устанавливать

    quotes = soup.select('.quote')
    for quote in quotes:
        text = quote.select('.text')[0].text[1:-1]
        author = quote.select('.author')[0].text
        author_link = quote.select('a')[0]['href']
        keywords = quote.select('.tags a')

        console.rule("[bold cyan]" + author)
        console.print(text)
        console.print(', '.join([tag.text for tag in keywords]), style='green on black')

        parsed[str(id)] =asdict(Quote(text=text,
                                      author=author,
                                      keywords=[tag.text for tag in keywords],
                                      autor_url=author_link))
        id += 1

    ref_next = soup.select('.next a')

with open(FILE_TO_SAVE, 'w', encoding='utf-8') as file:
    json.dump(parsed, file, ensure_ascii=False)

print(f'Обработано {len(parsed)} цитат на {page} страниц, результат в {FILE_TO_SAVE}')
