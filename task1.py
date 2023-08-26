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

from os import walk, path, listdir
import pathlib
import json

directory = "D:\GeekBrains\Advanced Python\homework\python-hw8"
# # def func_writer(dir):
# for i in walk(directory):
# for file in listdir():
#     print(file)






res_dict = {}



for dir_path, dir_name, file_name in walk(directory):
    ttl_size = 0
    for i in file_name:
        size = path.getsize(path.abspath(dir_path + '/' + i))
        ttl_size +=size
        print(f"{i} = {path.getsize(path.abspath(dir_path + '/' + i))} bytes")
    print(f'folder - {path.basename(dir_path)} has total size - {ttl_size}')


def 

    

    # for i in dir_name:
    #     print (i)    
    # print(path.getsize('task1.py'))
    # print(f'{dir_path = }\n{dir_name = }\n{file_name = }\n')
    # res_dict[f'dir - {dir_path}'] = [f'file - {file_name}, size - {path.getsize(file_name)}{file_name}'for i in file_name]
    # for i in file_name:
    #     print(path.getsize(i))
        

# with open (('json_file.json'), 'a', encoding='utf-8') as f:
#     data = json.dump(res_dict,f,indent=4)


