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
import apps
from victory import victorina
from apps import bank_cash
from time import ctime

apps.menu_print()
print()
print(f'Текущая директория: {os.getcwd()}')

while True:
    ctr = int(input('Введите пункт команды (пункт 13 - список команд): '))
    if ctr == 1:
        name_new_dir = input('Введите имя новой папки: ')
        if not os.path.exists(name_new_dir):
            os.mkdir(name_new_dir)
            print('Папка успешно создана! Возврат в главное меню.\n')
        else:
            print('Папка уже существует. Возврат в главное меню.\n')
    elif ctr == 2:
        name_del = input('Введите имя удаляемого объекта (example.txt для файла): ')
        try:
            if os.path.isdir(name_del):
                shutil.rmtree(name_del)
                print('Папка удалена! Возврат в главное меню.\n')
            else:
                os.remove(name_del)
                print('Файл удален! Возврат в главное меню.\n')
        except FileNotFoundError:
            print('Файл не найден. Возврат в главное меню.\n')
    elif ctr == 3:
        name_copy_src = os.path.basename(input('Введите имя копируемого объекта (example.txt для файла): '))
        name_copy_dst = os.path.basename(input('Введите путь назначения: '))
        try:
            if os.path.isdir(name_copy_src):
                shutil.copytree(name_copy_src, name_copy_dst)
            else:
                shutil.copy(os.path.abspath(name_copy_src), os.path.abspath(name_copy_dst))
                print('Файл скопирован успешно! Возврат в главное меню.\n')
        except FileNotFoundError:
            print('Файл не найден. Возврат в главное меню.\n')
    elif ctr == 4:
        work_dir = os.listdir(os.getcwd())
        for i in range(len(work_dir)):
            print(work_dir[i])
        print('Список содержимого выведен. Возврат в главное меню.\n')
    elif ctr == 5:
        work_dir = os.listdir(os.getcwd())
        print(f'Список папок в директории {os.getcwd()}:')
        for i in range(len(work_dir)):
            if os.path.isdir(work_dir[i]):
                print(work_dir[i])
        print()
    elif ctr == 6:
        work_dir = os.listdir(os.getcwd())
        print(f'Список файлов в директории {os.getcwd()}:')
        for i in range(len(work_dir)):
            if os.path.isfile(work_dir[i]):
                print(work_dir[i])
        print()
    elif ctr == 7:
        info_obj = os.path.join(os.getcwd(), input('Введите имя или путь объекта (example.txt для файла): '))
        try:
            info_ctime = os.path.getctime(info_obj)
            size = apps.get_size(path=info_obj)
            if os.path.isdir(info_obj):
                name_obj = 'Папка'
            else:
                name_obj = 'Файл'
            print(f'Размер {name_obj}: {size} байт. Дата создания: {ctime(info_ctime)}\n')
        except FileNotFoundError:
            print('Путь не найден. Возврат в главное меню.\n')
    elif ctr == 8:
        print('Ваша операционная система:')
        print(f'{sys.platform}\n')
        print('Возврат в главное меню.\n')
    elif ctr == 9:
        print('Программу написал: Екимов М.С.\n')
    elif ctr == 10:
        victorina()
        print('Возврат в файловый менеджер.\n')
    elif ctr == 11:
        bank_cash()
        print('Возврат в файловый менеджер.\n')
    elif ctr == 12:
        print(f'Текущая директория: {os.getcwd()}')
        try:
            os.chdir(os.path.join(os.getcwd(), input('Введите путь до директории: ')))
        except FileNotFoundError:
            print('Папка не найдена. Возврат в главное меню.\n')
        print(f'Текущая директория: {os.getcwd()}')
    elif ctr == 13:
        apps.menu_print()
    elif ctr == 14:
        break
    else:
        print('Неверный пункт меню!')
