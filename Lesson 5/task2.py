# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
# os.listdir(path=".") - список файлов и директорий в папке.

import sys
import os

dir_path = os.path.join(os.getcwd())
os.listdir(dir_path)
print('Папки в директории\n', os.listdir(dir_path))
