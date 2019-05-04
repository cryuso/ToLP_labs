print("Введите число a")
a = int(input())
print("Введите число b")
b = int(input())
print("Введите число c")
c = int(input())
print("Ведите число d")
d = int(input())
print("Ведите число f")
f = int(input())
rez = 0
if a == 0:
    print("Число a не может быть равно нулю")
    exit(1)
else:
    rez = abs(a-b*c*d**3+(c**5-a**2)/a+f**3*(a-213))
print("Результат вычислений равен ", rez)