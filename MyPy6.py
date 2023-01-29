num = input('Введите вещественное число: ')
count = 0

for i in num:
    if i != '.':
        count += int(i)
print(f'Полученная сумма цифр числа {num} равна: {count}')
