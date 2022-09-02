#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

#Пример:

#- A (3,6); B (2,1) -> 5,09
#- A (7,-5); B (1,-1) -> 7,21

print('Введите координаты точки A')
coordinate_A_X = float(input('X: '))
coordinate_A_Y = float(input('Y: '))

print('Введите координаты точки B')
coordinate_B_X = float(input('X: '))
coordinate_B_Y = float(input('Y: '))

distance_between_points = ((coordinate_A_X - coordinate_B_X)**2+(coordinate_A_Y - coordinate_B_Y)**2)**0.5
print('Расстояние между точками:') 
print (round(distance_between_points,3))