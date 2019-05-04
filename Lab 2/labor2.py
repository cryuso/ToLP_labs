string = 'дров, псов, план, курс, слов'
string = string.split(', ') #разбивает строку на части и возвращает в виде списка
for i in range(0, len(string)):
    if string[i][2] == 'о' and string[i][3] == 'в':
        print(string[i])