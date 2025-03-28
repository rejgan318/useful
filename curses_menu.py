import curses


def draw_menu(stdscr):
    # Список пунктов меню
    menu = ["Пункт 1", "Пункт 2", "Пункт 3", "Выйти"]
    # Текущая выборка
    current_row = 0

    # Отключение курсора
    curses.curs_set(0)

    while True:
        # Очистка экрана
        stdscr.clear()

        # Отрисовка меню
        for idx, row in enumerate(menu):
            if idx == current_row:
                # Отображение выбранного пункта
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(idx + 1, 1, row)
                stdscr.attroff(curses.color_pair(1))
            else:
                # Отображение невыбранных пунктов
                stdscr.addstr(idx + 1, 1, row)

        # Обновление экрана
        stdscr.refresh()

        # Обработка ввода
        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu) - 1:
            current_row += 1
        elif key == ord("\n"):  # Нажат Enter
            if menu[current_row] == "Выйти":
                break
            stdscr.addstr(len(menu) + 2, 1, f"Вы выбрали: {menu[current_row]}")
            stdscr.refresh()
            stdscr.getch()


def main():
    # Настройка цветов
    curses.wrapper(lambda stdscr: (
    curses.start_color(), curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_CYAN), draw_menu(stdscr)))


if __name__ == "__main__":
    main()