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
import sys
from os import mkdir, remove, rmdir, listdir
from shutil import copy
from victory import victorina
from bank_cash import bank_cash

# mkdir('test')
directory = os.getcwd()
print(directory)
# Разделение на папки и файлы. Можно папки и файлы сохранить в отдельные списки или сохранить в словарь
# разделение, сортировку и вывод можно убрать в функцию
list_dir = os.listdir(directory)
dict_dir = []
for d in range(len(list_dir)):
    if os.path.isdir(list_dir[d]):
        # print('Папка: ', list_dir[d])
        dict_dir.append('Папка: ' + list_dir[d])
    else:
        # print('Файл: ', list_dir[d])
        dict_dir.append('Файл: ' + list_dir[d])
# сортировка файлов и папок по алфавиту
dict_dir.sort()
print(dict_dir)
# вывод отсортированных файлов и папок. Строку в условии можно заменить на переменную.
for d in range(len(dict_dir)):
    if 'Файл' in dict_dir[d]:
        print(dict_dir[d])

print(sys.platform)

os.chdir(input('Введите путь: '))
directory = os.getcwd()
print(directory)
# print(os.path.isdir('bank_cash.py'))