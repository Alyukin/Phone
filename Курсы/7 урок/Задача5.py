stroka = input()
counter = 0
for step in range(len(stroka)):
    if stroka[step].isdigit() or stroka[step].isalpha():
        counter += 0
    else:
        counter += 1
        print('|', stroka[step], '|')
