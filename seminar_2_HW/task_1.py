"""
Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата
"""
BASE = 16

def to_hex(num):
    hex_digits = "0123456789ABCDEF"
    hex_str = ""
    
    if num == 0:
        return "0"
    
    while num > 0:
        remainder = num % BASE
        hex_str = hex_digits[remainder] + hex_str
        num = num // BASE
    
    return hex_str

num = int(input("Введите целое число: "))
hex_str = to_hex(num)
print(f"Шестнадцатеричное представление числа {num} равно: {hex_str}")
hex_result = hex(num)
print(f"Проверка по функции hex: {hex_result}")
