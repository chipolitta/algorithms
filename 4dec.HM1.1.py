# O(n)
def numberofsteps(num):
    a = 0                         # счетчик
    while num > 0:                # пока число больше нуля
        if num % 2 == 0:          # если число четное, то будем делить его на два
            num /= 2
            a += 1                # добавляется шаг
        else:                     # если число нечётное, то отнимаем единицу
            num -= 1
            a += 1                # добавляется шаг
    return a                      # возвращаем кол-во шагов