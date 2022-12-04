# O(n)
def numjewelsstones(jewels, stones):
    d = 0                                # счётчик
    for i in stones:                     # проходимся по камням
        if i in jewels:                  # если камень драгоценный, то добавляем в счётчик 1
            d += 1
    return d                             # возвращаем d