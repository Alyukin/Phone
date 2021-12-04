address = input()
address += ' '
index = 0
a = ''
counter = 0
for step in range(len(address)):

    if address[step] == '.':
        a = address[index:step]
        index = step + 1
        if a.isdigit():
            if 0 <= int(a) < 256:
                counter += 1

    elif address[step] == ' ':
        a = address[index:step]

        index = step + 1
        if 0 <= int(a) < 256:
            counter += 1

if counter == 4:
    print('IP адрес правильный')
else:
    print('IP адрес не правильный')