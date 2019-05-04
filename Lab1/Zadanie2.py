import random
print("Ведите левую границу диапазона значений")
lg = int(input())
print("Ведите правую границу диапазона значений")
r = int(input())
a = random.randint(lg, r)
print("Введите ваше число")
b = int(input())
m = False
while m is False:
    if a == b:
        print("Вы выиграли! :)")
        m = True
    else:
        if b < a:
            print("Ваше число меньше! Попробуйте ещё раз.")
            b = int(input())
        else:
            print("Ваше число больше! Попробуйте ещё раз.")
            b = int(input())
