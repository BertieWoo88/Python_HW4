'''
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
Затем пользователь вводит сами элементы множеств.
'''
from random import randint
getSring = [int(x) for x in input("введите два числа через пробел: ").split()]
print(getSring)
# n = int(input("введите размерность наборов чисел: "))
# m = int(input("введите размерность наборов чисел: "))
n = getSring[0]
m = getSring[1]

ListA = list( randint(0,20) for i in range(n))
ListB = list( randint(0,20) for i in range(m))

print(*ListA)    
print(*ListB)  

listF = list(set(ListA).intersection(set(ListB)))
listF.sort()
print(*listF)
