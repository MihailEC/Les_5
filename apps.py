import json
import random
import os


def transform_dict_list(menu):
    """
    Функция преобразования словаря в список ключ.значение.
    :param menu: на входе словарь keys-пункты меню, value-описание выполнения
    :return: список с элементами из строк ключ.значение
    """
    keys_menu = list(menu.keys())
    result = [f'{keys_menu[i]}. {menu[i + 1]}' for i in range(len(menu))]
    return result


def get_dir_size(path='.'):
    total = 0
    with os.scandir(path) as it:
        for p in it:
            if p.is_file():
                total += p.stat().st_size
            elif p.is_dir():
                total += get_dir_size(p.path)
    return total


def get_size(path='.'):
    if os.path.isfile(path):
        return os.path.getsize(path)
    elif os.path.isdir(path):
        return get_dir_size(path)


def dirs_work_list():
    """
    Функция определения директорий в рабочей папке
    :return: список директорий в папке
    """
    work_dir = os.listdir(os.getcwd())
    list_result = [work_dir[i] for i in range(len(work_dir)) if os.path.isdir(work_dir[i])]
    return list_result


def files_work_list():
    """
    Функция определения файлов в рабочей директории
    :return: список файлов в директории
    """
    work_dir = os.listdir(os.getcwd())
    list_result = [work_dir[i] for i in range(len(work_dir)) if os.path.isfile(work_dir[i])]
    return list_result


def save_listdir():
    """
    Сохраняет в файл listdir.txt строку с файлами и строку с папками.
    :return:
    """
    work_dir = os.listdir(os.getcwd())
    dirs = []
    files = []
    for i in range(len(work_dir)):
        dirs.append(work_dir[i]) if os.path.isdir(work_dir[i]) else files.append(work_dir[i])
    dirs = ', '.join(dirs)
    files = ', '.join(files)
    with open('listdir.txt', 'w', encoding='utf-8') as f:
        f.write(f'dirs: {dirs}\n')
        f.write(f'files: {files}')


def refill(cash, cash_up):
    """
    Функция банковского приложения. Добавляет к указанному счету сумму введенную пользователем.
    :param cash: Счет пользователя
    :return: возвращает увеличенный счет пользователя
    """
    if cash_up > 0:
        cash = cash + cash_up
        print('Счет пополнен.')
        return cash
    else:
        print('Сумма не может быть отрицательной!\n')
        return cash


def buy(cash, history_buy):
    """
    функция покупки. Выполняет списание со счета и запись в историю покупок.
    :param cash: передается счет пользователя
    :param history_buy: передается список истории покупок
    :return: возвращает измененный счет пользователя
    """
    buy_price = int(input('Введите сумму покупки: '))
    if buy_price > 0:
        if buy_price > cash:
            print('Недостаточно средств на счете')
            return cash
        else:
            name_buy = input('Введите название покупки: ')
            cash = cash - buy_price
            history_buy.append((name_buy, buy_price))
            print(f'Остаток средств: {cash}\n')
            return cash
    else:
        print('Сумма покупки не может быть отрицательной или равняться нулю!/n')
        return cash


def bank_cash():
    """
    Банковское приложение. Не имеет входных и выходных параметров.
    :return: Выводится меню по которому следует пользователь.
    """
    # Введение списка для истории покупок
    history_buy = []
    # чтение суммы на счету из файла
    if os.path.exists('cash.txt'):
        with open('cash.txt', 'r', encoding='utf-8') as f:
            cash = int(f.read())
    else:
        cash = 0
    # чтение истории покупок из файла
    if os.path.exists('history.txt'):
        with open('history.txt', 'r', encoding='utf-8') as f:
            history_buy = json.load(f)
    # тело программы (цикл с меню)
    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            try:
                cash_up = int(input('Введите сумму пополнения: '))
            except ValueError:
                print('Введите число!\n')
            else:
                cash = refill(cash, cash_up)
                print(f'Сумма на счету: {cash}\n')
        elif choice == '2':
            try:
                cash = buy(cash, history_buy)
            except ValueError:
                print('Введите число!\n')
                cash = buy(cash, history_buy)
        elif choice == '3':
            for el in history_buy:
                print('-'.join(map(str, el)))
            print()
            pass
        elif choice == '4':
            with open('cash.txt', 'w', encoding='utf-8') as f:
                f.write(f'{cash}')
            with open('history.txt', 'w', encoding='utf-8') as f:
                json.dump(history_buy, f)
            break
        else:
            print('Неверный пункт меню')


def victorina():
    # Входные данные в формате словаря

    born_date = {
        'Менделеев Д.И.': '08.02.1834',
        'Ломонсов М.В.': '19.11.1711',
        'Ковалевская С.Ф.': '15.01.1850',
        'Пирогов Н.И.': '25.11.1810',
        'Жуковский Н.Е.': '17.01.1847',
        'Басов Н.Г.': '14.12.1922',
        'Павлов И.П.': '26.09.1849',
        'Перельман Г.Я.': '13.06.1966',
        'Попов А.С.': '16.03.1859',
        'Черенков П.А.': '28.07.1904'
    }
    days = {
        '08': 'восьмое',
        '19': 'девятнадцатое',
        '15': 'пятнадцатое',
        '25': 'двадцать пятое',
        '17': 'семнадцатое',
        '14': 'четырнадцатое',
        '26': 'двадцать шестое',
        '13': 'тринадцатое',
        '16': 'шестнадцатое',
        '28': 'двадцать восьмое'

    }
    month = {
        '01': 'января',
        '02': 'февраля',
        '03': 'марта',
        '04': 'апреля',
        '05': 'мая',
        '06': 'июня',
        '07': 'июля',
        '08': 'августа',
        '09': 'сентября',
        '10': 'октября',
        '11': 'ноября',
        '12': 'декабря'
    }
    choice = 'Да'
    # # Цикл викторины.
    while choice == 'Да':
        count_good = 0
        count_persons = 5

        question_name = random.sample(list(born_date.keys()), count_persons)
        for j in range(len(question_name)):
            answer = input(f'Введите дату рождения {question_name[j]} в формате дд.мм.гггг: ')
            if born_date[question_name[j]] == answer:
                print('Дата рождения верна')
                count_good = count_good + 1
            else:
                question_date = born_date[question_name[j]].split('.')
                print(
                    f'Дата рождения неверна. Верный ответ: {days[question_date[0]]} {month[question_date[1]]} {question_date[2]} года.')

        # Подсчет и вывод количества верных и неверных ответов
        # count_bad = count_persons - count_good
        print(f'Количество верных ответов - {count_good}')
        print(f'Количество неправильных ответов - {count_good - count_persons}')
        choice = input('Начать викторину занаво? (Да/Нет): ')


if __name__ == '__main__':
    bank_cash()
    # victorina()