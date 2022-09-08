""" Задайте список из n чисел последовательности (1+1/n)**n выведите на экран их сумму. """

number = int(input('Введите число: '))

lst = []

for i in range(1, number + 1):
    lst.append(round((1 + 1 / i) ** i, 2))

sum = 0
for i in lst:
    sum += i

print(f'Сумма элементов списка {lst} = {round(sum,2)}')
