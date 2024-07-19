from pathlib import Path
from urllib.parse import unquote

import requests


def download_file(url: str, file_name: str = None, dir_name: str = None) -> str:
    """
    Downloads file from url and saves it in dir_name. Or return filename if file is exists

    :param url: The URL of the file to be downloaded.
    :param file_name: Optional. The desired name of the downloaded image file.
        If not provided, the name of the file in the URL will be used.
    :param dir_name: Optional. The directory where the image file should be saved.
        If it doesn't exist, it'll be created. If not provided, the file will be saved in the current working directory.
    :return: The downloaded file with dir_name.
    """

    dir_name = dir_name or ""
    file_name = file_name or unquote(Path(url).name)
    # name = Path(dir_name)

    if dir_name != "":
        Path(dir_name).mkdir(parents=True, exist_ok=True)

    result_file = Path(dir_name) / file_name
    if result_file.exists():
        return str(result_file)

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/97.0.4692.99 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f'Failed to download file. Server responded with status code {response.status_code}')

    with open(result_file, 'wb') as f:
        f.write(response.content)

    return str(result_file)


if __name__ == '__main__':
    url = "https://upload.wikimedia.org/wikipedia/commons/e/e0/Pythagoras_in_the_Roman_Forum%2C_Colosseum.jpg"
    # downloaded = download_img(url=url, dir_name="imgs/Pythagoras", file_name="Pyth.jpg")
    downloaded = download_file(url=url)
    print(downloaded)
