"""
1. Создать новый проект ""Консольный файловый менеджер"
2. В проекте реализовать следующий функционал:
После запуска программы пользователь видит меню, состоящее из следующих пунктов:
- создать папку; # реализуем с помощью os.mkdir
- удалить (файл/папку); # реализуем с помощью os.remove и shutil.rmtree
- копировать (файл/папку); # реализуем с помощью shutil.copy и
- просмотр содержимого рабочей директории; # реализуем с помощью os.list.dir
- посмотреть только папки; # реализуем с помощью os.path.isdir
- посмотреть только файлы; # реализуем с помощью os.path.isdir
- просмотр информации об операционной системе; # реализуем с помощью sys.platform
- создатель программы;
- играть в викторину;
- мой банковский счет;
- смена рабочей директории (*необязательный пункт); # реализуем с помощью os.chdir
- выход.
Так же можно добавить любой дополнительный функционал по желанию.

Используются функции из модуля ОС: mkdir, remove, rmdir, listdir
Используются функции из модуля shutil: copy

"""
import os
import shutil
import sys
from os import mkdir, remove, rmdir, listdir
from shutil import copy
from victory import victorina
from bank_cash import bank_cash

menu = {
    1: 'создать папку',
    2: 'удалить (файл/папку)',
    3: 'копировать (файл/папку)',
    4: 'просмотр содержимого рабочей директории',
    5: 'посмотреть только папки',
    6: 'посмотреть только файлы',
    7: 'просмотр информации об операционной системе',
    8: 'создатель программы',
    9: 'играть в викторину',
    10: 'мой банковский счет',
    11: 'смена рабочей директории',
    12: 'выход'
}
keys_menu = list(menu.keys())

print('Добро пожаловать в файловый менеджер.')
print('Команды:')
for i in range(len(menu)):
    print(f'{keys_menu[i]}. {menu[i + 1]}')
print()
print(f'Текущая директория: {os.getcwd()}')


while True:
    ctr = int(input('Введите пункт команды: '))
    if ctr == 1:
        name_new_dir = input('Введите имя новой папки: ')
        mkdir(name_new_dir)
    elif ctr == 2:
        name_del = input('Введите имя удаляемого объекта (example.txt для файла): ')
        try:
            if os.path.isdir(name_del):
                shutil.rmtree(name_del)
            else:
                os.remove(name_del)
        except FileNotFoundError:
            print('Файл не найден. Возврат в главное меню.\n')
    elif ctr == 3:
        pass
    elif ctr == 4:
        pass
    elif ctr == 5:
        pass
    elif ctr == 6:
        pass
    elif ctr == 7:
        pass
    elif ctr == 8:
        pass
    elif ctr == 9:
        pass
    elif ctr == 10:
        pass
    elif ctr == 11:
        pass
    elif ctr == 12:
        break
    else:
        print('Неверный пункт меню!')

# mkdir('test')
# directory = os.getcwd()
# print(directory)
# # Разделение на папки и файлы. Можно папки и файлы сохранить в отдельные списки
# # разделение, сортировку и вывод можно убрать в функцию
# list_dir = os.listdir(directory)
# dict_dir = []
# for d in range(len(list_dir)):
#     if os.path.isdir(list_dir[d]):
#         # print('Папка: ', list_dir[d])
#         dict_dir.append('Папка: ' + list_dir[d])
#     else:
#         # print('Файл: ', list_dir[d])
#         dict_dir.append('Файл: ' + list_dir[d])
# # сортировка файлов и папок по алфавиту
# dict_dir.sort()
# print(dict_dir)
# # вывод отсортированных файлов и папок. Строку в условии можно заменить на переменную.
# for d in range(len(dict_dir)):
#     if 'Файл' in dict_dir[d]:
#         print(dict_dir[d])
#
# print(sys.platform)
#
# os.chdir(input('Введите путь: '))
# directory = os.getcwd()
# print(directory)
# # print(os.path.isdir('bank_cash.py'))
