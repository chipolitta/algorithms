# O(n)
def minimumAbsDifference(self, arr):
    arr.sort()                                  # сортируем список по порядку
    difference = float('inf')
    for i in range(len(arr) - 1):
        if arr[i + 1] - arr[i] < difference:    # находим разницу, для элементов списка, если разность между двумя элементами < разницы
            difference = arr[i + 1] - arr[i]

    answer = []
    for i in range(len(arr) - 1):
        if arr[i + 1] - arr[i] == difference:   # если разность равна разнице, то дополняем список
            answer.append((arr[i], arr[i + 1]))
    return answer                               # возвращаем список