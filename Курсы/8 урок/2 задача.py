list1 = input().split()
bigger = []
for i in range(len(list1)):
    if int(list1[i]) > int(list1[i + 1]):
        bigger += list1[i]
print(bigger)
