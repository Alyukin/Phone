stroka = input()
a = stroka[:stroka.find('h')]
b = stroka[stroka.find('h'):stroka.rfind('h') + 1]
c = stroka[stroka.rfind('h') + 1:]
s = a + b[::-1] + c
print(stroka)
