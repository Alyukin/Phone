new_list = input().split()
counter = 0

for i in new_list:
    if int(i) > 0:
        counter += 1
print(counter)
