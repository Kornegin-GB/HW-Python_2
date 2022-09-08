""" Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
Пример:
6782 -> 23
0,56 -> 11
"""
import re

number = float(input('Введите число: '))

number = re.sub("[.|,| ]", "", str(number))  # Удаляем ненужные символы

result = 0

for i in number:
    result += int(i)

print(result)
