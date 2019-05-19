string = 'слов, пробелов, измениний, знаков, кошечка'
string = string.split(', ') #разбивает строку на части и возвращает в виде списка
for i in range(0, len(string)):
    if string[i][len(string[i])-1] == "в" and string[i][len(string[i])-2] == "о":
    #if string[i][-1] == "в" and string[i][-2] == "о":
        print(string[i])
