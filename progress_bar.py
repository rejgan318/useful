"""
progress bar
"""


def progress_bar(progress: float | int, total: float | int, symbol: str = '█', width: int = 100) -> None:
    """
    горизонтальный прогресс-бар
    :param progress: текущеее значение
    :param total: максимальное значение
    :param symbol: символ вывода прогресса
    :param width: ширина в символах
    :return:
    """
    print(f'{symbol * int(width * progress / total):.<{width}} {round(progress / total * 100):3}%', end='\r')

if __name__ == '__main__':
    import math

    print('😀😁😂🤣😃😄😅😆ꊠ黠だ')
    n = 100
    for i in range(n):
        result = math.factorial(i * 1000)
        # Win + . - select unicode char
        progress_bar(i+1, n, width=20)