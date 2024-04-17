"""Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем, используйте его строковое представление."""


def create_dictionary(**kwargs):
    """Создает словарь из ключевых параметров"""
    result_dict = {}
    for key, value in kwargs.items():
        result_dict[value] = key
    return result_dict

if __name__ == '__main__':
    print(create_dictionary(a=1, b='hello', c=(1, 2), d=3.14))

