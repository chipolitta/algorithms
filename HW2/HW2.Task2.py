# Получаем целое число - n, которое отвечает за размер массива. Задача решалась по формулам из условий.
# Сложность O(n)
def getMaximumGenerated(n: int) -> int:
    nums = [] # Создаем массив
    for i in range(n + 1):    # Проходимся по списку
        if 0 <= i <= 1:     # Условие задачи
            nums.append(i)    # Добавляем массив
        elif i % 2 == 0:    # Условие задачи
            nums.append(nums[i // 2])    # Если число четное
        else:
            nums.append(nums[i // 2] + nums[i // 2 + 1])   # Если число нечетное
    return max(nums)

getMaximumGenerated(7)