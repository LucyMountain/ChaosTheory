# x -> kx(1-x)

import matplotlib.pyplot as plt
import numpy

x_coord = []
y_coord = []

for k in numpy.arange(2.5, 4, 1e-3):
    x = 1 - 1 / k + 1e-7
    for i in range(1000):
        x = k * x * (1 - x)
    for i in range(500):
        x = k * x * (1 - x)
        x_coord.append(k)
        y_coord.append(x)

plt.scatter(x_coord, y_coord, s = 0.1)
plt.title("Logistic Map Phase Space")
plt.xlabel("k")
plt.ylabel("x")
plt.show()
