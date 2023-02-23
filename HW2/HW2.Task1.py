# Сложность - O(n*n)
# Будем решать метод перебора единиц
def countSquares(matrix) -> int:
    rows, cols = len(matrix), len(matrix[0])
    squares = 0     # Счётчик для квадратов
    for row in range(rows):     # Проходимся по строкам
        for col in range(1, cols):  # Проходимся по столбцам
            if row == 0:    # Условие
                break   # Прекращаем цикл
            matrix[row][col] *= min(matrix[row-1][col],
                                    matrix[row][col-1],
                                    matrix[row-1][col-1]) + 1
        squares += sum(matrix[row])
    return squares
countSquares([
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
])