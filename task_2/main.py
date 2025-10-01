n=int(input("Введите кол-во школьников: "))
k=int(input("Введите кол-во яблок: "))
apple = k // n
left = k - (n*apple)
print("Достанется ", apple, " яблок", 
"Останется ", left, " яблок")


