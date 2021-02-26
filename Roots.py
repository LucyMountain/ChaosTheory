from math import factorial
import matplotlib.pyplot as plt
import numpy

range_s = 3.141
range_e = 3.1412

a_list = []
b_list = []
x_list = []


def eix(x):
    a = 1 - (x ** 2 / factorial(2)) + (x ** 4 / factorial(4)) - (x ** 6 / factorial(6)) + (x ** 8 / factorial(8)) - (
                x ** 10 / factorial(10)) + (x ** 12 / factorial(12)) + 1
    b = x - (x ** 3 / factorial(3)) + (x ** 5 / factorial(5)) - (x ** 7 / factorial(7)) + (x ** 9 / factorial(9)) - (x ** 11 / factorial(11))
    return a, b

def testValues(range_s, range_e):
    for x in numpy.arange(range_s, range_e, ((range_e - range_s) / 100)):
        ans = eix(x)
        print(ans, x)
        a_list.append(ans[0])
        b_list.append(ans[1])
        x_list.append(x)

testValues(range_s, range_e)
"""
plt.plot(x_list, a_list, c = 'darkred')
plt.plot(x_list, b_list, c = 'aqua')
plt.show()
"""
