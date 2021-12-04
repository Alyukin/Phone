st = input()
st1 = st[st.find('h') + 1:st.rfind('h')]
st2 = st1.replace('h', 'H')
print(st[:st.find('h') + 1] + st1 + st[st.rfind('h'):])
