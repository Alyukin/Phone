two_dim_words = [['Kelvin', 'jungle'], ['cat'], ['dog', 'apple'], ['cat']]
list_2 = []
for i in range(len(two_dim_words)):
    if len(two_dim_words[i]) > 1:
        for step in range(len(two_dim_words[i])):
            list_2.append(two_dim_words[i][step])
    else:
        list_2.append(two_dim_words[i])
list_2.sort()
list_2.sort(key=len)
print(list_2)
