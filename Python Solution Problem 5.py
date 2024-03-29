#machine problem 5

from matplotlib import pyplot as plt
import numpy as np

nvalue = (range(0, 200))
n = np.array([range(0,200)])
x_equation = (input("Enter function x(n): "))
x_temp = eval(x_equation)
x = x_temp.transpose()

def xn (n):
    return eval(x_equation)

def yn (n):
    if n==0:
        return -1.5 * xn(n) + 2*xn(n+1) - 0.5 * xn(n+2)
    elif n > 0 and n <= 198:
        return 0.5 * xn(n+1) - 0.5 * xn(n-1)
    elif n == 199:
        return 1.5 * xn(n) - 2 * xn(n-1) + 0.5 * xn(n-2)

xvalue = x
yvalue = [yn(n) for n in nvalue]

plt.plot(nvalue, xvalue, 'm', label = 'Value of x(n)')
plt.plot(nvalue, yvalue, 'g', label = 'Value of y(n)')
plt.legend()
plt.show()