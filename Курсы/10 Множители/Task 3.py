a = {int(i) for i in input().split()}
b = {int(i) for i in input().split()}

c = a & b
print(sorted(c))
