x = int(input())
y = int(input())
n = int(input())
a = (n / (x + y)) * 2
if (n % (x + y)) > y:
    a = a + 2
elif (n % (x + y)) > 0:
    a = a + 1
print(int(a))
