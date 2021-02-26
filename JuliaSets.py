# Start at (a,b)
# (x,y) -> ((x**2)-(y**2)+a, 2xy+b)

import matplotlib.pyplot as plt
import numpy

x_coords = []
y_coords = []
for i in range(11):
    x_coords.append([])
    y_coords.append([])

# Put any two ints/floats in the next two lines between -2 and 2 (, )(, )(, )(, )(, )(, )(, )
c = -0.50092
d = 0.61932893493473

for a in numpy.arange(-2, 2, 5e-3):
    for b in numpy.arange(-2, 2, 5e-3):
        x = 0
        y = 0
        for iterations in range(101):
            oldx = x
            x = (x ** 2) - (y ** 2) + c
            y = (2 * oldx * y) + d
            if x ** 2 + y ** 2 > 4:
                break
        x_coords[int(iterations / 10)].append(a)
        y_coords[int(iterations / 10)].append(b)

plt.scatter(x_coords[0], y_coords[0], s = 0.1, c = 'darkred')
plt.scatter(x_coords[1], y_coords[1], s = 0.1, c = 'red')
plt.scatter(x_coords[2], y_coords[2], s = 0.1, c = 'orangered')
plt.scatter(x_coords[3], y_coords[3], s = 0.1, c = 'orange')
plt.scatter(x_coords[4], y_coords[4], s = 0.1, c = 'yellow')
plt.scatter(x_coords[5], y_coords[5], s = 0.1, c = 'greenyellow')
plt.scatter(x_coords[6], y_coords[6], s = 0.1, c = 'lime')
plt.scatter(x_coords[7], y_coords[7], s = 0.1, c = 'aqua')
plt.scatter(x_coords[8], y_coords[8], s = 0.1, c = 'blue')
plt.scatter(x_coords[9], y_coords[9], s = 0.1, c = 'indigo')
plt.scatter(x_coords[10], y_coords[10], s = 0.1, c = 'black')
plt.show()