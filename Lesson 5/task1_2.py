# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт. И второй скрипт, удаляющий эти папки.
# os.rmdir(path, *, dir_fd=None) - удаляет пустую директорию.
# os.removedirs(path) - удаляет директорию, затем пытается удалить родительские директории, и удаляет их рекурсивно, пока они пусты.
# os.mkdir(path, mode=0o777, *, dir_fd=None) - создаёт директорию. OSError, если директория существует.
# os.makedirs(path, mode=0o777, exist_ok=False) - создаёт директорию, создавая при этом промежуточные директории.
# os.remove(path, *, dir_fd=None) - удаляет путь к файлу.
# os.getcwd() - текущая рабочая директория.
# os.listdir(path=".") - список файлов и директорий в папке.


import sys
import os


def delete_dir(path):
    dir_path = os.path.join(os.getcwd(), path)
    os.removedirs(dir_path)
    print('директория {} удалена'.format(dir_path))


quantity_folder = [('dir_' + str(i + 1)) for i in range(9)]

for i in quantity_folder:
    delete_dir(i)
