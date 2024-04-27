import random

def check_attack(x1, y1, x2, y2):
    return x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2)

def check_queens(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if check_attack(arr[i][0], arr[i][1], arr[j][0], arr[j][1]):
                return False
    return True

def generate_queens_placement():
    queens_placement = []
    for _ in range(8):
        row = random.randint(1, 8)
        queens_placement.append((row, random.randint(1, 8)))
    return queens_placement
        

for i in range(4):
    queens = generate_queens_placement()
    while not check_queens(queens): 
        queens = generate_queens_placement()
    for queen in queens:
        print(queen)
    print(" ")

# вариант решения 1
# (4, 1)
# (8, 3)
# (3, 7)
# (1, 6)
# (5, 8)
# (6, 2)
# (2, 4)
# (7, 5)
# вариант решения 2
# (7, 3)
# (5, 8)
# (3, 2)
# (6, 1)
# (8, 6)
# (2, 4)
# (4, 5)
# (1, 7)
# вариант решения 3
# (1, 7)
# (8, 5)
# (6, 1)
# (7, 3)
# (2, 4)
# (3, 2)
# (5, 6)
# (4, 8)
# вариант решения 4
# (6, 5)
# (3, 7)
# (2, 4)
# (7, 2)
# (8, 8)
# (4, 1)
# (5, 3)
# (1, 6)