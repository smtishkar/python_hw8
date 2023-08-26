# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle.
# Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория.
# Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.

# Пример:
# test/users/names.txt
# Результат в json для names.txt:
# {
# "name": names.txt
# "parent": users,
# "type": "file"
# "size": 4096
# }
import json
import csv
from os import walk, path
import pickle

__all__ = ['folder_size_calc', 'walk_directory_func']


# подсчет общего размера папки
def folder_size_calc(directory: str) -> int:
    ttl_size = 0
    for dir_path, dir_name, file_name in walk(directory):
        for i in file_name:
            size = path.getsize(path.abspath(dir_path + '/' + i))
            ttl_size += size
    return ttl_size


directory = "C:\IT\GeekBrains\Python\homeworks\python_hw8"



def walk_directory_func(directory):
    res_dict = {}
    list_files = []
    data_csv = []
    for dir_path, dir_name, file_name in walk(directory):
        for i in dir_name:
            list_files.append(
                f'dir - {i} - size {folder_size_calc(dir_path + "/" + i)} bytes')
        for i in file_name:
            size = path.getsize(path.abspath(dir_path + '/' + i))
            list_files.append(f'file - {i} - size {size} bytes')
        res_dict[f'dir - {dir_path}'] = tuple(list_files)
        list_files.clear()

    with open(('json_file.json'), 'a', encoding='utf-8') as f:
        data = json.dump(res_dict, f, indent=4)
    for key, value in res_dict.items():
        data_csv.append([key, value])
    with open('csv_file.csv', 'w', newline='', encoding='utf-8') as csv_f:
        write_csv = csv.writer(csv_f, dialect='excel-tab', delimiter=',')
        write_csv.writerows(data_csv)
    with open('pickle_file.bin', 'wb') as pickle_file:
        pickle.dump(res_dict, pickle_file)


if __name__ == '__main__':
    walk_directory_func(directory)