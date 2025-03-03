""" Проверка системных hardlinks
Создаётся временный большой файл
Делается много его копий с помощью жёстких ссылок
Демонстрируется мгновенная скорость создание и то, что они не занимают место на диске
"""
from pathlib import Path
import shutil


def create_big_file(size_in_gb=1):
    fake_big_file = Path("temporary_big_file.bin")
    size_in_bytes = size_in_gb * 1024 ** 3

    # Записываем нули кусками
    chunk_size = 10 * 1024 * 1024  # 10 МБ
    with fake_big_file.open("wb") as f:
        bytes_written = 0
        zeros_chunk = b"\0" * chunk_size  # Буфер из нулей
        while bytes_written < size_in_bytes:
            remaining = size_in_bytes - bytes_written
            write_size = min(chunk_size, remaining)
            f.write(zeros_chunk[:write_size])
            bytes_written += write_size

    return fake_big_file


size = 10
print(f"Create big file {size} GB...")
big_file = create_big_file(size)
print(f"Создан файл {big_file}, размер {big_file.stat().st_size / (1024 ** 3):.3f} ГБ")

path = Path("/")
usage = shutil.disk_usage(path)
print(f"Общий объём текущего диска: {usage.total / (1024 ** 3):.3f} ГБ")
used = usage.used
free = usage.free
print(f"Занято: {used / (1024 ** 3):.3f} ГБ")
print(f"Свободно: {free / (1024 ** 3):.3f} ГБ")

n = 10
file_names = [big_file.with_stem(big_file.stem + f"_hardlink_{i:02}") for i in range(n)]

# делаем жёсткие ссылки на созданный раннее большой фейковый файл
for file in file_names:
    file.hardlink_to(big_file)
    print(f"создана ссылка {file}")

usage = shutil.disk_usage(path)
print(f"После создания {n} жёстких ссылок на {size * n} GB\n"
      f"Занято: {usage.used / (1024 ** 3):.3f} ГБ; "
      f"прирост = {usage.used - used:,} (должен быть 0 или около того)")

print("Удаляем временные файлы")
for file in file_names + [big_file]:
    file.unlink()
