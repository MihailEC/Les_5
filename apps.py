import random
import os


def menu_print():
    menu = {
        1: 'создать папку',
        2: 'удалить (файл/папку)',
        3: 'копировать (файл/папку)',
        4: 'просмотр содержимого рабочей директории',
        5: 'посмотреть только папки',
        6: 'посмотреть только файлы',
        7: 'получить информацию об объекте',
        8: 'просмотр информации об операционной системе',
        9: 'создатель программы',
        10: 'играть в викторину',
        11: 'мой банковский счет',
        12: 'смена рабочей директории',
        13: 'вызов списка команд',
        14: 'выход'
    }

    keys_menu = list(menu.keys())
    print('Добро пожаловать в файловый менеджер.')
    print('Команды:')
    for i in range(len(menu)):
        print(f'{keys_menu[i]}. {menu[i + 1]}')


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

def refill(cash):
    """
    Функция банковского приложения. Добавляет к указанному счету сумму введенную пользователем.
    :param cash: Счет пользователя
    :return: возвращает увеличенный счет пользователя
    """
    cash_up = int(input('Введите сумму пополнения: '))
    if cash_up > 0:
        cash = cash + cash_up
        print('Счет пополнен.')
        return cash
    else:
        print('Неверное значение суммы!\n')
        pass


def buy(cash, buy_price):
    """
    Функция банковского приложения. Вычитает из счета пользователя сумму покупки.
    :param cash: Счет пользователя
    :param buy_price: Сумма покупки
    :return: Возвращает измененный счет пользователя
    """
    if buy_price > 0:
        if buy_price > cash:
            print('Недостаточно средств на счете')
            pass
        else:
            cash = cash - buy_price
            return cash
    else:
        print('Сумма покупки не может быть отрицательной или равняться нулю!\n')


def bank_cash():
    """
    Банковское приложение. Не имеет входных и выходных параметров.
    :return: Выводится меню по которому следует пользователь.
    """
    cash = 0
    history_buy = []
    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            try:
                cash = refill(cash)
                print(f'Сумма на счету: {cash}\n')
            except ValueError:
                print('Введите число!\n')
                pass
        elif choice == '2':
            buy_price = int(input('Введите сумму покупки: '))
            try:
                cash = buy(cash, buy_price)
                name_buy = input('Введите название покупки: ')
                history_buy.append([name_buy, buy_price])
                print(f'Покупка совершена. Остаток средств: {cash}\n')
            except ValueError:
                print('Введите число!\n')
                pass
        elif choice == '3':
            for el in history_buy:
                print('-'.join(map(str, el)))
            print()
            pass
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')


def victorina():
    # Входные данные в формате строки

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
                print(f'Дата рождения неверна. Верный ответ: {days[question_date[0]]} {month[question_date[1]]} {question_date[2]} года.')

        # Подсчет и вывод количества верных и неверных ответов
        # count_bad = count_persons - count_good
        print(f'Количество верных ответов - {count_good}')
        print(f'Количество неправильных ответов - {count_good - count_persons}')
        choice = input('Начать викторину занаво? (Да/Нет): ')

if __name__ == '__main__':
    bank_cash()
    victorina()
