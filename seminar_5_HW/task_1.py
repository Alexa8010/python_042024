"""Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла."""

def split_path(file_path: str)-> tuple:
    """Сплитует путь до файла в кортеж"""
    parts = file_path.split('/')
    file_name_with_extension = parts[-1]
    path =  ""
    for item in parts[:-1]:
        path += item + "/"
    file_name_parts = file_name_with_extension.split('.')
    file_name = file_name_parts[0]
    file_extension = '.' + file_name_parts[1] 
    return (path, file_name, file_extension,)

file_path = "/home/user/Documents/GB/Sem_5_HW.py"
result_tuple = split_path(file_path)
print(result_tuple) 



def split_path(file_path):
    parts = file_path.split('/')
    file_name_with_extension = parts[-1]
    path =  ""
    for item in parts[:-1]:
        path += item + "/"
    
    file_name_parts = file_name_with_extension.split('.')
    file_name = file_name_parts[0]
    file_extension = '.' + file_name_parts[1] 
        
    return (path, file_name, file_extension,)

file_path = "/home/user/Documents/GB/Sem_5_HW.py"
result_tuple = split_path(file_path)
print(type(result_tuple)) 