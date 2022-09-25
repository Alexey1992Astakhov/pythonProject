#5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними
#в 2D пространстве. https://ru.onlinemschool.com/math/library/analytic_geometry/point_point_length/

x_1 = int(input("Введите число x_1: "))
y_1 = int(input("Введите число y_1: "))
x_2 = int(input("Введите число x_2: "))
y_2 = int(input("Введите число y_2: "))

print(f"{((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2) ** 0.5:0.4}")