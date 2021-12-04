n = int(input())
if n == 0:
    print(0)
else:
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    print(b)


a = int(input())
b = 1
x = 0
for c in range(2, a):
    b = x + b
    x = b
print(b)


a = int(input())
b = 1
x = 0
for c in range(a-2):
    x, b = b, x + b

print(b)


n = int(input())
if n == 0:
    print(0)
else:
    a, b =0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    print(b)


n = int(input())
i = 1
if n < 0:
    print("n должно быть отрицательным")
else:
    print("n должно быть положительным")
while i ** 2 <= n:
    print(i ** 2)
    i += 1