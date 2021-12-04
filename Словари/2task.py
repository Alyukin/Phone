a = int(input())
b = {}
for i in range(a):
    first, second = input().split()
    b[first] = second
    b[second] = first
print(b(input()))
