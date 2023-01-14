# Fractal 1 - Chaos Game

import matplotlib.pyplot as plt
from numpy import random

corners_x = [0, 1, 0, 1]
corners_y = [0, 0, 1, 1]
x_coords = [1/3]
y_coords = [1/3]
x = 1/3
y = 1/3
point = 0
point_new = 0

for i in range(0, 10**6):
    while point_new == point:
        point_new = random.randint(0, 3)
    point = point_new
    x = 0.5 * (x + corners_x[point])
    y = 0.5 * (y + corners_y[point])
    x_coords.append(x)
    y_coords.append(y)

plt.scatter(x_coords, y_coords, s = 0.1, c = 'blue')
plt.show()
