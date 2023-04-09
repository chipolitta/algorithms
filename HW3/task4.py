# сложность O(mn), где m - количество строк, а n - количество столбцов в матрице
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0 # проверка наличия матрицы, если ее нет, то выводим 0

        islands = 0
        visited = set()

        for row in range(len(grid)): # проходимся по каждой ячейке матрицы
            for col in range(len(grid[0])): # если 0 - следуящая ячейка, если 1 - вызов функции explore
                islands += self.explore(grid, row, col, visited) # поиск острова, который содержит данную ячейку

        return islands

    def explore(self, grid, row, col, visited):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[row]) or grid[row][col] == "0" or (
        row, col) in visited: # проверяем, является ли ячейка частью острова, если нет
            return 0 # возвращаем 0

        visited.add((row, col)) # если часть острова - посещенная

        self.explore(grid, row + 1, col, visited) # проверка соседних ячеек
        self.explore(grid, row - 1, col, visited)
        self.explore(grid, row, col + 1, visited)
        self.explore(grid, row, col - 1, visited)

        return 1
