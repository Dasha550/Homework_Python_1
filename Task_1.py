#1.Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

#Пример:

#- 6 -> да
#- 7 -> да
#- 1 -> нет

Day_of_the_week = int(input('Введите цифру, обозначающую день недели: '))
if Day_of_the_week<=5:
    print('Будний день')
else:
    print('Выходной день')