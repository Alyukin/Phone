a = input().split()
c = set(a)
for i in a:
    if i in c:
        print('ДА')
        c.discard(i)
    else:
        print('НЕТ')
