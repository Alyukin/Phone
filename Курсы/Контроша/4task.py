counter = 0
while counter == 0:
    float_number = input()
    if float_number.isdigit() == False:
        continue
    else:
        if float_number.isdigit():
            print('Ок')
        else:
            print('Вещественное')
