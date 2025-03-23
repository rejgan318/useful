"""
Коды нажатия клавиш для использования в opencv waitKeyEx. Определены все клавиши для стандартной клавиатуры.
Можно добавить недостающие клавиши, в т.ч. Кириллицу, комбинации Shift +...
Пример использования ниже, запускайте
"""
import enum


class Key(enum.IntEnum):

    F1 = 0x700000
    F2 = 0x710000
    F3 = 0x720000
    F4 = 0x730000
    F5 = 0x740000
    F6 = 0x750000
    F7 = 0x760000
    F8 = 0x770000
    F9 = 0x780000
    F10 = 0x790000
    F11 = 0x7a0000
    F12 = 0x7b0000

    N1 = 0x31
    N2 = 0x32
    N3 = 0x33
    N4 = 0x34
    N5 = 0x35
    N6 = 0x36
    N7 = 0x37
    N8 = 0x38
    N9 = 0x39
    N0 = 0x30

    # В нижнем регистре только для наглядности, чтобы не путать с Shift + ...
    a = 0x61
    b = 0x62
    c = 0x63
    d = 0x64
    e = 0x65
    f = 0x66
    g = 0x67
    h = 0x68
    i = 0x69
    j = 0x6a
    k = 0x6b
    l = 0x6c
    m = 0x6d
    n = 0x6e
    o = 0x6f
    p = 0x70
    q = 0x71
    r = 0x72
    s = 0x73
    t = 0x74
    u = 0x75
    v = 0x76
    w = 0x77
    x = 0x78
    y = 0x79
    z = 0x7a

    Enter = 0xd
    Esc = 0x1b
    Tab = 0x9
    BackSpace = 0x8

    #            Not supported in cv
    # NumLock = 0x900000
    # Shift = 0x100000
    # ScrollLock = 0x110000
    # Pause = 0x130000
    # Control = 0x200000
    # Alt = 0x400000
    # CapsLock = 0x140000

    Left = 0x250000
    Right = 0x270000
    Up = 0x260000
    Down = 0x280000
    PgUp = 0x210000
    PgDown = 0x220000
    Home = 0x240000
    End = 0x230000
    Insert = 0x2d0000
    Delete = 0x2e0000

    Period = 0x2e
    Comma = 0x2c
    Semicolon = 0x3b
    Quote = 0x27
    Backquote = 0x60
    Underscore = 0x5f
    Leftbracket = 0x5b
    Rightbracket = 0x5d
    Backslash = 0x5c

    Space = 0x20
    Plus = 0x2b
    Minus = 0x2d
    Equal = 0x3d
    Asterisk = 0x2a
    Slash = 0x2f


if __name__ == '__main__':
    import cv2 as cv
    import numpy as np

    help_text = "Press any key, F1 for help, ESC to exit"
    cv.namedWindow(help_text, cv.WINDOW_AUTOSIZE)
    # Без imshow waitKeyEx не работает, поэтому что-то выводим. Это окно должно быть активно, результат в терминале
    cv.imshow(help_text, np.ones((20, 400, 3), np.uint8) * 128)
    print(help_text)
    while True:
        key_pr = cv.waitKeyEx(0)
        match key_pr:
            case Key.Esc:
                break
            case Key.F1:
                print("Help file not found! :-)")
            case _:
                print(f"{Key(key_pr).name if key_pr in Key else 'Not found':10} {key_pr:7} {key_pr:7x}")

    cv.destroyAllWindows()
