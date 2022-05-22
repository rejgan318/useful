"""
Парсинг сайта goodreads
"""
from bs4 import BeautifulSoup
import requests
from rich.console import Console


def get_one_quote(quote) -> dict:
    """
    Парсим одну цитату
    :param quote:
    :return: parsed info
    """
    text = quote.select('.quoteText')[0].text.split('―')[0].strip()[1:-1]
    author = quote.select('.authorOrTitle')[0].text.strip()
    tags = ','.join([tag.text.strip() for tag in quote.select('.quoteFooter .left a')])
    return {'text': text, 'author': author, 'tags': tags}


def get_page_quotes(url: str) -> list[dict]:
    """
    Парсим одну страниу
    :param url: адрес парсинга
    :return: список распарсингованных цитат на странице
    """
    response = requests.get(url)
    if response.status_code != 200:
        return None
    soup = BeautifulSoup(response.text, 'html.parser')
    # parsed_page = []
    # quotes = soup.select('.quote')
    # for quote in quotes:
    #     parsed_page.append(get_one_quote(quote))
    parsed_page = [get_one_quote(quote) for quote in soup.select('.quote')]
    # next_url = None if soup.select('.next_page.disabled') else soup.select_one('.next_page')['href']
    next_url = soup.select_one('.next_page').get('href', None)
    return parsed_page, next_url


console = Console()
base_url = '^'
print('Go!')
parsed = []
url = base_url + '/quotes'
# url = base_url + '/quotes?page=99'
page = 1
while True:
    with console.status(f"Страница {page:3}", spinner='dots', spinner_style='red on black'):
        page_quotes, next_url = get_page_quotes(url)
    parsed += page_quotes
    if next_url:
        url = base_url + next_url
    else:
        break
    page += 1

print(f'Итого {len(parsed)}')

# while True:
#     if page > 1:
#         url = f"{base_url}{ref_next[0].attrs['href']}"
#     else:
#         url = base_url
#     # print(f'Страница {page}: {url}')
#     style = "bold white on blue"
#     with console.status(f'Страница {page}: {url}', spinner='arrow', spinner_style=style):
#         response = requests.get(url)
#         soup = BeautifulSoup(response.text, 'html.parser')
#
#     quotes = soup.select('.quote')
#     for quote in quotes:
#         text = quote.select('.text')[0].text
#         author = quote.select('.author')[0].text
#         author_link = quote.select('a')[0]['href']
#         if authors.get(author, None) is None:
#             authors[author] = author_link
#         keywords = quote.select('.tags a')
#         for keyword in keywords:
#             tags.add(keyword.text)
#         console.rule("[bold cyan]" + author)
#         console.print(text)
#         # console.print(f"Автор [cyan bold]{author}")
#         console.print(', '.join([tag.text for tag in keywords]), style='green on black')
#
#     ref_next = soup.select('.next a')
#     if not ref_next:
#         break
#     page += 1

print('Приехали!')
