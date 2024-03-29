"""
Generates a python program source file that can be used to create a binary file from a base64 string.
"""
import base64
from pathlib import Path

program_template = \
    """# Generated by generate_py_from_bin.py
# Make file '{name_file}' from binary data there (optionally) and return binary data
from base64 import b64decode


def make_binary_file(name: str = None):
    data = {data}
    if name:
        with open(name, 'wb') as f:
            f.write(b64decode(data))


if __name__ == '__main__':
    make_binary_file('{name_file}')
"""


def generate_py_from_bin(binary_file_name: str, python_file_name: str = None) -> str:
    """
    Генерация python-программы, которая содержит в себе байтовую строку, соответствующую
    бинарному файлу данных

    - Прочитать файл данных;
    - преобразовать в base64;
    - разбить на строки (отформатировать с помощью reformat_long_str);
    - сгенерировать python-программу с помощью шаблона program_template;
    - сохранить в виде файла на диске с именем python_file_name

    :param binary_file_name: Файл данных, **должен существовать**
    :param python_file_name: Имя файла сгенерированной программы. Если не указано,
        формируется как имя файла данных без пути к файлу; с заменой точки на _; расширение .py
    :return: python_file_name, переданное как параметр или сгенерированное
    """

    def reformat_long_str() -> str:
        """
        Format a long string so that it can be pasted into a python file.

        :return: multiline python byte string
        """
        delimiter = "' \\\n    b'"
        width = 100  # symbols per line

        fragments = [b64_string[i:i + width] for i in range(0, len(b64_string), width)]
        return delimiter.join(fragments)

    assert Path(binary_file_name).exists(), f"File {binary_file_name} does not exist"

    python_file_name = python_file_name or f"make_{Path(binary_file_name).stem}_{Path(binary_file_name).suffix[1:]}.py"

    with open(binary_file_name, 'rb') as f_bin, open(python_file_name, 'w') as f_py:
        binary_data = f_bin.read()
        b64_string = str(base64.b64encode(binary_data))
        data = reformat_long_str()
        python_src = program_template.format(name_file=binary_file_name, data=data)
        f_py.write(python_src)

    return python_file_name


if __name__ == '__main__':
    BINARY_FILE_NAME = 'data/small_probe.png'

    generated_file = generate_py_from_bin(BINARY_FILE_NAME)
    print(f"Abraham begat Isaac; and Isaac begat Jacob...\nLook at {generated_file} from {BINARY_FILE_NAME}")
