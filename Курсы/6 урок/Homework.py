st = str(input())
ind = 0
count = ''
the_big = ''
for step in range(len(st)):
    if st[step] == ' ':
        count = st[ind:step]
        ind = st + 1
        if len(count) > len(the_big):
            the_big = count
print(the_big)
