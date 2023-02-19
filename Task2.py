# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

n = int(input('Введите количество элементов в массиве: '))
import random
 
rand_list=[]
for i in range(n):
    rand_list.append(random.randint(-10,10))
print(rand_list)

min_number = int(input())
max_number = int(input())
for i in range(len(rand_list)):
    if min_number <= rand_list[i] <= max_number:
        print(i)