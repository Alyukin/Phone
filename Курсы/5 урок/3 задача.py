a = int(input())
b = 0
while a >= 1:
    if a % 2 == 1:
        b += 1
    a = a // 2
print(b)
