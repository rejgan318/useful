"""
Парсинг https://quotes.toscrape.com
По мотивам https://www.geeksforgeeks.org/quote-guessing-game-using-web-scraping-in-python/
"""
from bs4 import BeautifulSoup
import requests
from rich.console import Console

console = Console()

base_url = 'https://quotes.toscrape.com'
page = 1
print('Go!')
authors = {}
tags = set()

while True:
    if page > 1:
        url = f"{base_url}{ref_next[0].attrs['href']}"
    else:
        url = base_url
    # print(f'Страница {page}: {url}')
    style = "bold white on blue"
    with console.status(f'Страница {page}: {url}', spinner='arrow', spinner_style=style):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

    quotes = soup.select('.quote')
    for quote in quotes:
        text = quote.select('.text')[0].text
        author = quote.select('.author')[0].text
        author_link = quote.select('a')[0]['href']
        if authors.get(author, None) is None:
            authors[author] = author_link
        keywords = quote.select('.tags a')
        for keyword in keywords:
            tags.add(keyword.text)
        console.rule("[bold cyan]" + author)
        console.print(text)
        # console.print(f"Автор [cyan bold]{author}")
        console.print(', '.join([tag.text for tag in keywords]), style='green on black')

    ref_next = soup.select('.next a')
    if not ref_next:
        break
    page += 1

print('Приехали!')
