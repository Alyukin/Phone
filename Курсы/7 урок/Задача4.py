stroka = input()
counter = 0
for step in range(len(stroka)):
    if stroka[step].isdigit():
        counter += 1
print(counter)
