# Напишите программу, которая принимает на вход число 
# N и выдает набор произведений чисел от 1 до N

n = int(input('Введите число для вычисления факториала: '))
 
factorial = 1
print('[', end = '')
for i in range(1, n + 1):
    if i != n:
        factorial *= i
        print(f'{factorial}, ', end = '')    
    else:
        factorial *= i
        print(f'{factorial}', end = '')

print(']', end = '')
print(f'\nФакториал числа {n} равен: {factorial}')

 

