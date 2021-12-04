import matplotlib.pyplot as pit

x = list(range(-5, 6))
y = [x1 ** 3 for x1 in x]

plt.plot(x, y, label='y(x)=x^3')
plt.xlabel('x')
plt.grid(True)
plt.legend()
plt.show()