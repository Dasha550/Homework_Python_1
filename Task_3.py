#Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

#Пример:

#- x=34; y=-30 -> 4
#- x=2; y=4-> 1
#- x=-34; y=-30 -> 3
print('Введите координаты точки')
coordinate_X = int(input('X: '))
coordinate_Y = int(input('Y: '))

if coordinate_X!=0 and coordinate_Y!=0 and coordinate_X>0 and coordinate_Y>0:
    print('Первая четверть')
elif coordinate_X!=0 and coordinate_Y!=0 and coordinate_X<0 and coordinate_Y>0:
    print('Вторая четверть')
elif coordinate_X!=0 and coordinate_Y!=0 and coordinate_X<0 and coordinate_Y<0:
    print('Третья четверть')
else:
    print('Четвёртая четверть')
