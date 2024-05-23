"""
make icon sheet from directory jpg
"""

from PIL import Image
from pathlib import Path
import math


def create_icon_table(image_paths, cols, icon_size, output_path):
    # Распакуем размер иконок
    icon_width, icon_height = icon_size

    # Определим количество строк
    total_images = len(image_paths)
    rows = math.ceil(total_images / cols)   # округление вверх

    # Создаем новое изображение для таблицы
    table_image = Image.new('RGB', (cols * icon_width, rows * icon_height), (255, 255, 255))

    # Заполняем таблицу иконками
    for idx, img_path in enumerate(image_paths):
        # Загружаем изображение иконки
        img = Image.open(img_path)
        # Изменяем размер изображения, сохраняя пропорции
        img.thumbnail((icon_width, icon_height))

        # Создаем пустую картинку с белым фоном для вставки
        icon_img = Image.new('RGB', (icon_width, icon_height), (255, 255, 255))

        # Центрируем изображение
        img_w, img_h = img.size
        paste_x = (icon_width - img_w) // 2
        paste_y = (icon_height - img_h) // 2
        icon_img.paste(img, (paste_x, paste_y))
        # Вычисляем позицию иконки в таблице
        row = idx // cols
        col = idx % cols

        # Вычисляем координаты вставки
        x = col * icon_width
        y = row * icon_height

        # Вставляем иконку в таблицу
        table_image.paste(icon_img, (x, y))

    # Сохраняем результирующее изображение
    table_image.save(output_path)


image_folder = Path(r'd:\dev\data\testpict')
image_paths = list(image_folder.rglob('*.jpg'))
create_icon_table(image_paths=image_paths, cols=4, icon_size=(200, 200), output_path='icon_table.jpg')
