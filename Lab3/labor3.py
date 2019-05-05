import os
f = open('Products.txt', 'r') #открыть для чтения
product = []

for line in f:
    line = line.strip() #удаление пробельных символов в начале и конце строки
    line = line.split(';') #разбиение строки по разделению
    product.append([line[0], line[1], line[2], line[3]]) #добавляет эл-т в конец списка
maxi = int(len(product)) #кол-во товаров


#Задание 1 (Узнать кол-во файлов в папке)


def count(): #инструкция, определяющая функцию
    path = input('Введите путь к папке: ')
    files = next(os.walk(path)) #возврат файлов
    print('Количество файлов в папке: ', len(files))

    print('---------------------------------------------------------------\n'
          '1 - Повторить программу\n'
          '2 - Меню\n'
          '---------------------------------------------------------------\n')
    cont = input('Выберете команду: ')
    if cont == "1":
        count()
    elif cont == "2":
        menu()

#Задание 2 (Сортировка)


def sor():
    print('Сортировка по:\n',
          '1 - Названию (A-Z) - дороже 1700\n',
          '2 - Названию (Z-A) - дороже 1700')
    a = input('Выберете команду: ')
    if a == '1':
        print('                Таблица:')
        product.sort(key=lambda line: str(line[1]))
        for i in range(0, len(product)):
            if int(product[i][2]) > 1700:
                print(product[i])
    elif a == '2':
        print('                Таблица:')
        product.sort(key=lambda line: str(line[1]), reverse=True)
        for i in range(0, len(product)):
            if int(product[i][2]) > 1700:
                print(product[i])
    else:
        print('Неверная команда!')
        sor()

    print('---------------------------------------------------------------\n'
          '1 - Повторить программу\n'
          '2 - Меню\n'
          '---------------------------------------------------------------\n')
    cont = input('Выберете команду: ')
    if cont == "1":
        sor()
    elif cont == "2":
        menu()
    return product

#Задание 3 (Уменьшение цены)


def price():
    NUM = [] #список
    print('                Таблица:')
    for i in range(0, len(product)):
        print(product[i])
    print('0 - Далее')

    work = True
    while work is True:
        num = input('Введите номер товара: ')
        if num.isdigit(): #содержит ли строка только цифры?
            num = int(num)
            if num == 0:
                work = False
            elif num <= maxi:
                NUM.append(num)
            else:
                print('Такого номера не существует! Максимальный номер:', maxi)
                work = True
        else:
            print('Неверный символ! Повторите попытку.')
            work = True

    minus = int(input('Введите значение, на которое нужно уменьшить цену: '))
    for i in range(0, len(product)):
        for j in range(0, len(NUM)):
            if int(product[i][0]) == int(NUM[j]): #если номер товара равен введеному номеру
                product[i][2] = int(product[i][2]) - minus

    print('Изменения сохранены!\n'
          '         Новая таблица: ')
    for i in range(0, len(product)):
        print(product[i])

    print('---------------------------------------------------------------\n'
          '1 - Повторить программу\n'
          '2 - Меню\n'
          '---------------------------------------------------------------\n')
    cont = input('Выберете команду: ')
    if cont == "1":
        price()
    elif cont == "2":
        menu()
    return product

#Задание 4 (Сохранение результата)


def savage():
    print('                 Где сохранить результат?\n'
          '---------------------------------------------------------------\n'
          '1 - Сохранить в этом документе\n'
          '2 - Сохранить в новом документе\n'
          '---------------------------------------------------------------\n')
    a = input('Выберете команду: ')

    if a == '1':
        file = open('Products.txt', 'r+') #открыт для чтения и записи
        for i in range(0, len(product)):
            for j in range(0, len(product[i])):
                if 0 <= j <= 2:
                    file.write(str(product[i][j]) + ";") #запись в файл
                else:
                    file.write(str(product[i][j]))
            file.write('\n')
        print('Файл Products.txt успешно сохранен!')
        file.close()

    if a == '2':
        name = input('Введите название файла: ')
        new = open(name, 'w') #открытие на запись, содержимое файла удаляется, если файла не существует, создается новый
        for i in range(0, len(product)):
            for j in range(0, len(product[i])):
                if 0 <= j <= 2:
                    new.write(str(product[i][j]) + ";")
                else:
                    new.write(str(product[i][j]))
            new.write('\n')
        print('Файл ', name, ' успешно сохранен!')
        new.close()

    print('---------------------------------------------------------------\n'
          '1 - Повторить программу\n'
          '2 - Меню\n'
          '---------------------------------------------------------------\n')
    cont = input('Выберете команду: ')
    if cont == "1":
        savage()
    elif cont == "2":
        menu()

#МЕНЮ


def menu():
    print('------------------------------МЕНЮ------------------------------\n'
          '1 - Задание 1 - Открыть файл\n'
          '2 - Задание 2 - Сортировка по названию\n'
          '3 - Задание 3 - Уменьшение цены\n'
          '4 - Задание 4 - Сохранить изменения\n'
          '0 - Выход из программы\n'
          '----------------------------------------------------------------\n')
    a = input('Выберете команду: ')

    if a == "1":
        count()
    elif a == "2":
        sor()
    elif a == "3":
        price()
    elif a == "4":
        savage()
    elif a == "0":
        print('                     Пока! :)')
        exit()
    else:
        print('Неверная команда!')
        menu()


menu()

f.close()
