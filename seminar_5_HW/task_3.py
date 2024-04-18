""" Создайте функцию генератор чисел Фибоначчи"""

def is_fibonacci(number: int) -> bool:
    """Подтверждает принадлежность к последовательности Фибоначчи"""
    a, b = 0, 1
    while a < number:
        a, b = b, a + b
        if number == a:
            return True
    return False

def generate_fibonacci():
    count = 0
    while True:
        if is_fibonacci(count):
            yield count
        count += 1

j = generate_fibonacci()
for _ in range(int(input("введите число N: "))):
    print(next(j), end=' ')
