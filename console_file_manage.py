import os, shutil, sys, apps
from time import ctime

menu = {
    1: 'создать папку',
    2: 'удалить (файл/папку)',
    3: 'копировать (файл/папку)',
    4: 'просмотр содержимого рабочей директории',
    5: 'сохранить содержимое рабочей директории в файл',
    6: 'посмотреть только папки',
    7: 'посмотреть только файлы',
    8: 'получить информацию об объекте',
    9: 'просмотр информации об операционной системе',
    10: 'создатель программы',
    11: 'играть в викторину',
    12: 'мой банковский счет',
    13: 'смена рабочей директории',
    14: 'вызов списка команд',
    15: 'выход'
}

print('Добро пожаловать в файловый менеджер.\nКоманды:')
for item in apps.transform_dict_list(menu):
    print(item)
print(f'\nТекущая директория: {os.getcwd()}')

while True:
    ctr = int(input('Введите пункт команды (пункт 14 - список команд): '))
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
        apps.save_listdir()
        print()
    elif ctr == 6:
        print(f'Список папок в директории {os.getcwd()}:')
        for item in apps.dirs_work_list():
            print(item)
        print()
    elif ctr == 7:
        print(f'Список файлов в директории {os.getcwd()}:')
        for item in apps.files_work_list():
            print(item)
        print()
    elif ctr == 8:
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
    elif ctr == 9:
        print(f'\nВаша операционная система: {sys.platform} \nВозврат в главное меню.\n')
    elif ctr == 10:
        print('\nАвтор программы: Екимов М.С.\n')
    elif ctr == 11:
        apps.victorina()
        print('Возврат в файловый менеджер.\n')
    elif ctr == 12:
        apps.bank_cash()
        print('Возврат в файловый менеджер.\n')
    elif ctr == 13:
        print(f'Текущая директория: {os.getcwd()}')
        try:
            os.chdir(os.path.join(os.getcwd(), input('Введите путь до директории: ')))
        except FileNotFoundError:
            print('Папка не найдена. Возврат в главное меню.\n')
        print(f'Текущая директория: {os.getcwd()}')
    elif ctr == 14:
        for item in apps.transform_dict_list(menu):
            print(item)
    elif ctr == 15:
        break
    else:
        print('Неверный пункт меню!')