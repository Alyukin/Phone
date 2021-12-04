text = input().split()
book_1 = {x: 0 for x in text}
x = 0
for code in book_1.keys():
    for i in range(len(text)):
        if code == text[i]:
            x += 1
        book_1[code] = x
    x = 0

sorted_val = sorted(book_1.values(), reverse=True)
for step in sorted_val:
    for k, z in book_1.items():
        if step == z:
            print(k, z)
#print(book_1)
