"""
Чтение и запись файла с позиционированием, прямой доступ
В качестве исходного файла берется интерпретатор Python.
Копирование файла за две операции в обратном порядке,
сравнение файлов путем вычисления контрольных сумм.
"""
import hashlib
import sys
from pathlib import Path

SOURCE_FILE = sys.executable
NEW_FILE = "new_python" + Path(SOURCE_FILE).suffix
file_size = Path(SOURCE_FILE).stat().st_size
FRACTION = 3
position = file_size // FRACTION   # точка для двух операций чтения и записи. Можно // 2, тогда две части будут равными

def calculate_md5_checksum(file_path):
    """ Вычислить контрольную сумму файла """
    hash_md5 = hashlib.md5()    # можно использовать hashlib.sha256()
    with open(file_path, 'rb') as file:
        # итератор, который вызывает лямбда-функцию до тех пор, пока она не вернёт пустую строку (b""),
        # что свидетельствует об окончании файла.
        for chunk in iter(lambda: file.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def get_bar(sym1, sym2):
    return f"{' data1 ':{sym1}^{int(80 / FRACTION)}}|{' data2 ':{sym2}^{80 - int(80 / FRACTION)}}"


print(f"Read file {SOURCE_FILE}, size = {file_size}")
print(get_bar('-', '-'))
with open(SOURCE_FILE, "rb") as f:
    f.seek(position)
    print(f"Read data2: from position {position} to end file, size = {file_size - position},")
    print(get_bar('-', 'r'))
    data2 = f.read(file_size - position)
    print(f"Read data1: from begin file to {position}, size = {position}")
    print(get_bar('r', 'r'))
    f.seek(0)
    data1 = f.read(position)

assert len(data1) + len(data2) == file_size

with open(NEW_FILE, "wb") as f:
    print(f"Creating new file {NEW_FILE} size = {file_size}")
    f.truncate(file_size)
    print(f"Write data2 from position {position} to end, size = {len(data2)}")
    print(get_bar('r', 'w'))
    f.seek(position)
    f.write(data2)
    print(f"Write data1 from begin, size = {len(data1)}")
    print(get_bar('w', 'w'))
    f.seek(0)
    f.write(data1)

print("Calculate and compare md5 checksums for source file and copied file")
assert calculate_md5_checksum(SOURCE_FILE) == calculate_md5_checksum(NEW_FILE)
print(f"Ok, files match. Delete {NEW_FILE}")
Path(NEW_FILE).unlink()
