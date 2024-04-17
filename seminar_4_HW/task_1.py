"""Напишите функцию для транспонирования матрицы
"""

def transpose_matrix(matrix: list[list]) -> list[list]:
    """Транспонирует матрицу"""    
    transposed_matrix = []
    for j in range(len(matrix[0])):
        transposed_row = []
        for i in range(len(matrix)):
            transposed_row.append(matrix[i][j])
        transposed_matrix.append(transposed_row)
    
    return transposed_matrix

if __name__ == '__main__':
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]


print(transpose_matrix(matrix))