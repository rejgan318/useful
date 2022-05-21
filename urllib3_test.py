"""
https://urllib3.readthedocs.io/en/stable/
https://pypi.org/project/urllib3/
https://pythonist.ru/biblioteka-urllib3-python/

Библиотека urllib3 — это мощный HTTP-клиент на Python c простым для понимания и продуманным кодом.
Она поддерживает безопасность потоков, пул соединений, проверку SSL / TLS на стороне клиента,
загрузку файлов с многокомпонентным кодированием, создание повторных запросов и работу с редиректом HTTP,
архивирование и разархивирование, а также прокси для HTTP и SOCKS.
"""
import urllib3

http = urllib3.PoolManager()
url = 'http://webcode.me'
resp = http.request('GET', url)
print(resp.status)
print(resp.data.decode('utf-8'))
