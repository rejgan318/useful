"""
rich - пример использования
pip install rich
https://github.com/Textualize/rich
https://rich.readthedocs.io/en/stable/introduction.html
"""
import math
from rich.console import Console
from rich.progress import track


def do_step(step):
    res = math.factorial(step * 1000)


console = Console()
# специяльные последовательности для отображения символов юникода по их именам
# Не отображаются в окне выполнения pycharm
console.print(":smiley: :vampire: :pile_of_poo: :thumbs_up: :raccoon:")

# крсивый прогресс-бар
for step in track(range(100)):
    do_step(step)
