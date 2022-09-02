#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


num_X = int(input('Введите число X: '))
num_Y = int(input('Введите число Y: '))
num_Z = int(input('Введите число Z: '))

if not(num_X or num_Y or num_Z) == (not num_X) or (not num_Y) or (not num_Z):
    print('Утверждение истинное')
else:
    print('Утверждение не истинно')