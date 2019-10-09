# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

# os.rmdir(path, *, dir_fd=None) - удаляет пустую директорию.
# os.removedirs(path) - удаляет директорию, затем пытается удалить родительские директории, и удаляет их рекурсивно, пока они пусты.
# os.mkdir(path, mode=0o777, *, dir_fd=None) - создаёт директорию. OSError, если директория существует.
# os.makedirs(path, mode=0o777, exist_ok=False) - создаёт директорию, создавая при этом промежуточные директории.
# os.remove(path, *, dir_fd=None) - удаляет путь к файлу.
# os.getcwd() - текущая рабочая директория.
# os.listdir(path=".") - список файлов и директорий в папке.


import sys
import os

def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


#print('sys.argv = ', sys.argv)


do = {"mkdir": make_dir}
try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None