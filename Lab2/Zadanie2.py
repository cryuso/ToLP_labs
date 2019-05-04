my_string = "        Ф;И;О;               О студенте" \
            ";_Иванов;Иван;Иванович; Студент 3 курса, 23 года"\
            ";_Петров;Семен;Игоревич; Студент 2 курса, 22 года"
my_string = my_string.split(';_')
for i in range(0, len(my_string)):
    string = my_string[i]
    string = string.split(';')
    print(string[0] + ' ' + string[1] + ' ' + string[2] + '     ' + string[3] + '     ')
