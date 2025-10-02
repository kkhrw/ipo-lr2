import math
#Вариант 2
a = float(input("Введите длину стороны а: "))
b = float(input("Введите длину стороны b: "))
c = float(input("Введите длину стороны c: "))
d = float(input("Введите длину стороны d: "))
p = (a+b+c+d)/2
s = ((a+b)/(math.fabs(a-b)))*math.sqrt((p-a)*(p-b)*(p-a-c)*(p-a-d))
print("Площадь трапеции: ", s)