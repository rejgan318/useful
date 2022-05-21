"""
progress bar
"""


def progress_bar(progress, total, symbol='█', width=100):
    print(f'{symbol * int(width * progress / total):.<{width}} {round(progress / total * 100):3}%', end='\r')

if __name__ == '_main_':
    import math
    n = 100
    for i in range(n):
        result = math.factorial(i * 1000)
        progress_bar(i+1, n, width=20, symbol='*')