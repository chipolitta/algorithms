# Решаем по условию задачи. Нужно понять как долго снижалась акция.
# Сложность - O(n)
def getDescentPeriods(prices) -> int:
    smooth = len(prices) # Создаем переменную с массивом
    smooth1, smooth2 = 0, 0     # Счётчик
    for i in range(1, len(prices) + 1):     # Проходимся по элементам
        if i != len(prices) and prices[i - 1] - prices[i] == 1:    # Условие
            smooth1, smooth2 = smooth1 + 1, smooth2 + smooth1
            continue    # Продолжаем
        smooth += smooth1 + smooth2
        smooth1, smooth2 = 0, 0
    return smooth
getDescentPeriods([8, 6, 7, 7])