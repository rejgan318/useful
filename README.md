# useful Полезности, тесты, эксперименты

## Что здесь?

Полезности и сервис, красивый вывод
- [Простой самописный progress bar](#progress_barpy)
- [colorama](#colorama_testpy)
- [rich progress bar](#rich_testpy)
- [argparse, pathlib](#argparse_test)

Тысты библиотек
- [urllib3](#urllib3_testpy)
- [BeautifulSoup, парсинг](#beautifulsoup)
- [Pygame](#pygame_lesson3py)
- [speech_recognition, pyttsx3, webbrowser](#speech_recognition_saypy)

## Полезности и сервис, красивый вывод

### progress_bar.py 
простой однострочный прогресс-бар с параметрыми
### colorama_test.py
Тест цвета и позиции курсора
### rich_test.py
При устанвке Emulate terminal нормально отображается прогресс-бар в Pycharm, но не выводятся символы юникода. И наоборот. 
В новом терминале Windows (PowerShell и cmd) отображается все корректно

![](imgs/pycharm_set_configuration.jpg)

- Console - с выводом символов юникода по символическим именам
- track - красивый прогресс-бар

### [argparse_test](argparse_test.py)
Тест на argpase и pathlib

## Тeсты библиотек

### urllib3_test.py
Библиотека urllib3 — это мощный HTTP-клиент на Python c простым для понимания и продуманным кодом.
Она поддерживает безопасность потоков, пул соединений, проверку SSL / TLS на стороне клиента,
загрузку файлов с многокомпонентным кодированием, создание повторных запросов и работу с редиректом HTTP,
архивирование и разархивирование, а также прокси для HTTP и SOCKS.

[PyPi](https://pypi.org/project/urllib3/),
[Документация](https://urllib3.readthedocs.io/en/stable/),
[Статья на русском](https://pythonist.ru/biblioteka-urllib3-python/)

### BeautifulSoup
**BeautifulSoup/pasemachine_lesson1.py** - один из уроков парсинга сайтов с помощью BeautifulSoup 
[Отсюда](https://parsemachine.com/articles/urok-1-pishem-parser-kataloga-tovarov-na-python/), 
[github](https://github.com/parsemachine/lessons/commit/77dad3c71e1e3675b644c63022d7b7c59a190000),
[Youtube](https://www.youtube.com/watch?v=PcIYQXOa4jw)

**BeautifulSoup/scraping_quotes.py** парсинг сайта, модифицированный пример с [geeksforgeeks](https://www.geeksforgeeks.org/quote-guessing-game-using-web-scraping-in-python/)

**BeautifulSoup/parsing_goodreads.py** - еще одна заготовка парсинга сайта [www.goodreads.com](https://www.goodreads.com)

### pygame_lesson3.py 
Тест библиотеки Pygame, простейшие операции

### speech_recognition_say.py
- speech_recognition получения аудиопотока, распознования голоса
- pyttsx3 воспроизведение текста
- webbrowser запуск броузера

### base64
**generate_make_file_py.py** Generates a python program source file that can be used to create a binary file from a base64 string.

data/small_probe.png input binary file 
