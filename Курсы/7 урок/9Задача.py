stroka = input()
if stroka.count('f') == 1:
    print(-1)
elif stroka.count('f') < 1:
    print(-2)
else:
    print(stroka.find('f', stroka.find('f') + 1))
