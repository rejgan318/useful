"""

"""
import argparse
import pathlib
import sys


def get_args(parameters: str = ''):
    parser = argparse.ArgumentParser(description='Get list of files and directories',
                                     epilog='Enjoy with Total Commander! :)')
    parser.add_argument('files',
                        nargs='+',
                        # type='str',
                        # type='pathlib.Path',
                        help='Список файлов и директорий')
    if len(sys.argv) > 1:
        args = parser.parse_args()
    else:
        args = parser.parse_args(parameters.split())
    return args


def get_all_files(files: list[str], recursive: bool = True) -> list[str]:
    """
    из списка файлов и директорий получить список только файлов, заменив директории на список всех файлов,
    которые в них содержатся
    :param files: список файлов и директорий
    :param recursive: fale - не учитывать вложенные директории
    :return: списко файлов без директорий
    """
    mask = '**/*.*' if recursive else '*.*'
    res = []
    for file in files:
        res.extend([file] if pathlib.Path(file).is_file() else list(map(str, pathlib.Path(file).glob(mask))))
    return res


def main():
    args = get_args(r'c:\Users\eugene\dev\pytondev\printscreenscr\testpict\anna '
                    r'c:\Users\eugene\dev\pytondev\printscreenscr\testpict\62_.jpg '
                    r'c:\Users\eugene\dev\pytondev\printscreenscr\testpict\63_.jpg ')
    files = get_all_files(args.files, recursive=False)
    print("Файлов ", len(files))
    print(pathlib.PurePath(__file__).parent, pathlib.PurePath(__file__).name)
    print(pathlib.Path(__file__).with_name('settings.ini'))
    _ = input('Press Enter')  # for debug
    print('Done.')


if __name__ == '__main__':
    main()
