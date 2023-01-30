# Реализуйте алгоритм перемешивания списка

import random
lst = []

for i in range(random.randint(3,10)):
    lst.append(random.randint(0,100))
print(f'Изначальный список: {lst}')

for i in range(len(lst)):
    rand_index = random.randint(0, len(lst) - 1)
    accum = lst[i]
    lst[i] = lst[rand_index]
    lst[rand_index] = accum
print(f'Перемешанный список: {lst}')