"""
Сохранить список float чисел в файле в двоичном формате и прочитать их
"""
import struct

BIN_FILE = 'data/floats.bin'

# Ваш список чисел с плавающей точкой
float_list = [3.14, 2.718, 1.618, 0.577]

# Открываем файл для записи в бинарном режиме
with open(BIN_FILE, 'wb') as f:
    # Проходим по каждому числу в списке и записываем его в файл
    for number in float_list:
        # Упаковываем число с плавающей точкой в формат 'f' (4 байта)
        f.write(struct.pack('f', number))

# Открываем файл для чтения в бинарном режиме
with open(BIN_FILE, 'rb') as f:
    # Создаем пустой список для хранения прочитанных чисел
    float_list_read = []

    # Читаем по 4 байта (размер одного числа с плавающей точкой в формате 'f')
    while chunk := f.read(4):
        # Распаковываем 4 байта и добавляем число в список
        float_list_read.append(round(struct.unpack('f', chunk)[0], 3))

print(float_list)
print(float_list_read)