# Вернуть максимальную сумму денег, которую грабитель может ограбить.
# Сложность O(n)
def rob(nums) -> int:
    def robber(nums, start, end): # Создаем функцию, которая будет отвечать за грабителя
        sum1 = 0    # Первый дом
        sum2 = 0    # Второй дом
        for step in range(start, end):  # Перебираем с начала и до конца
            current_house = nums[step]  # Сколько в текущем доме есть денег
            sum1, sum2 = sum2 + current_house, max(sum1, sum2) # Пересчитываем
        return max(sum1, sum2)

    if not nums:    # Условие
        return 0
    elif len(nums) == 1:    # Если количество домов равно 1
        return nums[0]
    else:
        n = len(nums)   # Количество домов равно длине домов
        return max(robber(nums, 1, n), robber(nums, 0, n - 1)) # Максимальное из двух возможных вариантов


rob([1, 2, 3, 4, 5, 6, 7])