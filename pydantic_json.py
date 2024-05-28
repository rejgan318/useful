"""
Создать модель pydantic, сделать json из нее, из json создать новую модель.
Модель сложнее обычной, содержит вложенную модель pydantic
"""
from pydantic import BaseModel


class Face(BaseModel):
    region_id: int


class Photo(BaseModel):
    """Содержит список вдложенных моделей"""
    name: str
    faces: list[Face] = []


vasya = Photo(name='Вася Пупкин', faces=[Face(region_id=1), Face(region_id=2)])
print(f"Фото Василия создано конструктором, просто печать:\n{vasya}\n")

vasya_dict = vasya.model_dump()
print(f"Создадим словарь model_dump(): \n{vasya_dict}\n")
vasya_from_dict = Photo(**vasya_dict)
print(f"Копия Василия, созданная из dict:\n{vasya_from_dict}\n")

vasya_json_str = vasya.model_dump_json(indent=2)    # indent только для наглядности, можно опустить
print(f"Создадим строку json model_dump_json():\n{vasya_json_str}\n")
# Созданный json как строку можно сохранить в текстовом файле обычным write, а позже прочитать read
vasya_from_json = Photo.model_validate_json(vasya_json_str)
print(f"Копия Василия, созданная из json:\n{vasya_from_json}\n")

print("...еще пара примеров:")
print(Photo.model_validate_json('{"name": "Васисуалий Лоханкин", "faces": [{"region_id": 1958}]}'))
print(Photo(**{"name": "Зубейда"}))
