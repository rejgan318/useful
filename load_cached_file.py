"""
load_cached_file - загрузка файлa по ссылке из интернета или из кеша если скачан ранее.
"""
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError


def load_cached_file(
    url: str,
    cache_dir: str | Path = "data/cache",
    filename: str | None = None,
    timeout=30,
    headers=None
) -> Path:
    """
    Возвращает путь к файлу из кеша.
    Если файла нет — скачивает его по URL и сохраняет в cache_dir.

    :param url: Прямая ссылка на файл
    :param cache_dir: Директория кеша внутри проекта
    :param filename: Имя файла в кеше. Если не задано, берётся из URL
    :return: Path к локальному файлу
    :param timeout: служебное, для настройки времени ожидания ответа от сервера
    :param headers: служебное, пользовательские заголовки для запроса
    """
    cache_dir = Path(cache_dir)
    cache_dir.mkdir(parents=True, exist_ok=True)

    if filename is None:
        filename = url.split("/")[-1].split("?")[0] or "downloaded_file"

    file_path = cache_dir / filename

    if file_path.exists() and file_path.stat().st_size > 0:
        return file_path

    headers = headers or {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0.0.0 Safari/537.36"
        ),
        "Accept": "image/avif,image/webp,image/apng,image/*,*/*;q=0.8",
        "Referer": "https://commons.wikimedia.org/",
    }

    request = Request(url, headers=headers)

    try:
        with urlopen(request, timeout=timeout) as response:
            data = response.read()
            if not data:
                raise ValueError(f"Пустой ответ при загрузке файла: {url}")
            file_path.write_bytes(data)
    except HTTPError as e:
        raise RuntimeError(
            f"Не удалось скачать файл. HTTP ошибка {e.code}: {e.reason}. "
            f"Попробуйте другой URL или проверьте ограничения сервера."
        ) from e
    except URLError as e:
        raise RuntimeError(f"Не удалось скачать файл из-за сетевой ошибки: {e.reason}") from e

    return file_path


if __name__ == '__main__':
    # сайт для тестирования загрузки файлов https://proof.ovh.net/files
    url = "https://proof.ovh.net/files/1Mb.dat"
    # При первом запуске создаётся директория, в которую загружается файл При последующих запусках файл загружается
    # из локального кеша. Можно явно указать имя файла
    path = load_cached_file(url, cache_dir="cache/")
    print(f"Файл загружен: {path}")