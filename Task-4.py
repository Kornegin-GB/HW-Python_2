""" Задайте числами список из N элементов, заполненных из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число. """

from random import randint

n = int(input("N = "))

lst = []

for i in range(-n, n + 1):
    lst.append(i)

with open('file.txt', 'w') as number:
    i = 0
    while i < n:
        number.write(f'{randint(0, n * 2)}\n')
        i += 1

print(lst)

mult = 1

with open('file.txt', 'r') as number:
    for i in number.read():
        if i != '\n':
            print(i, end=' ')
            mult *= lst[int(i)]

print(f'\nПроизведение = {mult}')
