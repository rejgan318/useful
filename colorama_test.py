""" https://pypi.org/project/colorama/ """

from colorama import Fore, Back, Style, init, Cursor
from time import sleep, time

tb = time()

init()
print(f'Поехали...{Fore.BLUE}Номного синего {Back.GREEN}и с зеленым фоном'
      f'{Fore.RESET}{Back.RESET} '
      f'{Style.BRIGHT}немного яркого{Style.NORMAL} обычный')
print(f'Нестандартный {Fore.LIGHTRED_EX}свето-{Style.BRIGHT}красный{Style.NORMAL}{Fore.RESET} цвет')

ForeRED = '\x1b[31m'
ForeRESET = '\x1b[39m'
print(f'Немного {ForeRED}красного текста{ForeRESET} через ESC-последовалености без colorama')
input('Press Enter')
fan = ["-", "\\", "|", "/"]
delay = 0.2
print(Cursor.POS(1, 1)+' '*100, end='')
print(Cursor.POS(1, 2)+' '*100, end='')
print(Cursor.POS(1, 3)+' '*100, end='')
print(Cursor.UP(2))
print(r"  -----=------   ")
print(r" /            \  ")
print(r"===( )=====( )===", end="")
roll_imdex = 0

for i in range(5):
    print(f"{Cursor.BACK(13)}{fan[roll_imdex]}{Cursor.FORWARD(7)}{fan[roll_imdex]}{Cursor.FORWARD(4)}", end="")
    roll_imdex = roll_imdex + 1 if roll_imdex < len(fan) - 1 else 0
    sleep(delay)
te = time() - tb

print('\nDone')
print('Будет затерто')
print(Cursor.UP(1)+'Затерли выше ')
