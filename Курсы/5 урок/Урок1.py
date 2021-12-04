n = int(input())
for i in range(1, n + 1):
    for a in range(1, i + 1):
        print(a, sep='', end='')
    print()

a = int(input())
sum = 0
i = 0
b = 0
while a != 0:
    sum += a
    a = int(input())
    i += 1
b = (sum / i)
print(b)

max_value = 0
element = -1
while element != 0:
    element = int(input())
    if element > max_value:
        max_value = element
print(max_value)

x = int(input())
z = 0
y = 0
while x != 0:
    if x == z and x > y:
        z = x
        y += x
    x = int(input())
print(y)

x = int(input())
y = 0

while x != 0:
    z = x % 10
    if z > y:
        y = z
    x //= x // 10
print(y)