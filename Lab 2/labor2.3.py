n = int(input('Введите длину списка (>10): '))
list = []
for i in range(0, n):
    list.append(int(input('Введите элемент ' + str(i+1) + ' : '))) #добавляет эл-т в конец списка
print('Ваш список: ', list)
list.append(int(input('Введите первый новый элемент: ')))
list.append(int(input('Введите второй новый элемент: ')))
list.append(int(input('Введите третий новый элемент: ')))
list.append(int(input('Введите четвертый новый элемент: ')))
list.append(int(input('Введите пятый новый элемент: ')))
list = [x for x in list if x % 2 != 0] #создает новый список, где каждый эл-т обозначается как х и нечетный
print('Ваш новый список: ', list)
