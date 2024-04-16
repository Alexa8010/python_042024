"""
Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. Определите какие вещи
влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант.
*Верните все возможные варианты комплектации рюкзака.
"""

items = {
    'спальник': 3,
    'еда':  2,
    'палатка': 4,
    'термос':  1,
    'котелок': 2,
}

max_weight = 7

total_weight = 0
backpack = []

for item in items:
    if total_weight + items[item] <= max_weight:
        backpack.append(item)
        total_weight += items[item]

for item in backpack: 
    print(f'{item} (масса: {items[item]})')