"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню

2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню

3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню

4. выход
выход из программы

При выполнении задания можно пользоваться любыми средствами

Для реализации основного меню можно использовать пример ниже или написать свой
"""





def refill(cash):
    cash_up = int(input('Введите сумму пополнения: '))
    # global cash
    if cash_up > 0:
        cash = cash + cash_up
        print('Счет пополнен.')
        return cash
        # print(f'Счет пополнен. Сумма на счету: {cash}\n')
    else:
        print('Неверное значение суммы!\n')
        pass


def buy(cash, buy_price):
    # global cash
    # global history_buy
    # buy_price = int(input('Введите сумму покупки: '))
    if buy_price > 0:
        if buy_price > cash:
            print('Недостаточно средств на счете')
            pass
        else:
            # name_buy = input('Введите название покупки: ')
            cash = cash - buy_price
            # history_buy.append((name_buy, buy_price))
            # print(f'Остаток средств: {cash}\n')
            return cash

    else:
        print('Сумма покупки не может быть отрицательной или равняться нулю!\n')

def get_list_buy(history_buy, buy_price):
    name_buy = input('Введите название покупки: ')
    history_buy.append((name_buy, buy_price))
    return history_buy

def bank_cash():
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
                buy_list = get_list_buy(history_buy, buy_price)
                history_buy.append(buy_list)
                print(f'Остаток средств: {cash}\n')
            except ValueError:
                print('Введите число!\n')
                pass
        elif choice == '3':
            print(history_buy)
            # for l in history_buy:
            #     print(l)
                # for i in range(len(l)):
                #     print(i, i + 1)
                #     print(l[i], ':')
                # print(l[1], '-', l[2])
            print()
            pass
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')

if __name__ == '__main__':
    bank_cash()