from pydantic import BaseModel
from itertools import groupby
from typing import List, Dict
from operator import itemgetter

# Определяем модель Pydantic
class Item(BaseModel):
    category: str
    name: str


# Создаем список объектов
items = [
    Item(category='fruit', name='apple'),
    Item(category='fruit', name='banana'),
    Item(category='vegetable', name='carrot'),
    Item(category='vegetable', name='potato'),
    Item(category='fruit', name='pear'),
]

# Сортируем список по полю, по которому будем группировать
items.sort(key=lambda x: x.category)

# Группируем список по полю category
grouped = groupby(items, key=lambda x: x.category)

# Преобразуем результат в словарь
grouped_dict = {key: list(group) for key, group in grouped}

# Вывод результата
for key, value in grouped_dict.items():
    print(f"{key}:")
    for fruit in value:
        print(f"\t{fruit.name}")
