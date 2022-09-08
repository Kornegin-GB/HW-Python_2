""" Реализуйте алгоритм перемешивания списка """

from random import randint

lst = [1, 2, 3, 4, 5, 6]

new_lst = []

for i in lst:
    new_lst.insert(randint(0, len(lst) - 1), i)

print(lst)
print(new_lst)
