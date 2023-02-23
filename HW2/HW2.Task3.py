# Сложность - O(n)
# Решаем по условию задачи
def uniquePathsWithObstacles(obstacleGrid) -> int:
    if not obstacleGrid:    # Условие
        return
    m, n = len(obstacleGrid), len(obstacleGrid[0])  # Количество строк и столбцов

    paths = [[0] * n for row in range(n)]   # Создаем новую матрицу
    paths[0][0] = 1     # Ставим робота
    for row in range(m):    # Проходимся по строкам
        for col in range(n):    # Проходимся по столбцам
            if obstacleGrid[row][col] or (row == 0 and col == 0):   # Условие
                continue    # Продолжаем
            paths[row][col] = (paths[row-1][col] if row else 0) + (paths[row][col-1] if col else 0)
    return paths[m-1][n-1]

uniquePathsWithObstacles([[0,1],[0,0]])