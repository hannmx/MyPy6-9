# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму
list_res = []   #создание пустого списка
n = int(input('Введите количество чисел последовательности: '))

for i in range (1, n + 1):  #цикл для заполнения списка значениями последовательности
    list_res.append(round((1+1/i)**i, 2))
print(f'Последовательность: {list_res}\nСумма последовательности: {sum(list_res)}')
