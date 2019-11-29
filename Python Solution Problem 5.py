#machine problem 5

from matplotlib import pyplot as plt
import math as math 

nvalue = list(range(0, 200))

def xn (n):
    return math.sin((3 * math.pi * n) / 100)

def yn (n):
    if n==0:
        return -1.5 * xn(n) + 2*xn(n+1) - 0.5 * xn(n+2)
    elif n > 0 and n < 198:
        return 0.5 * xn(n+1) - 0.5 * xn(n-1)
    elif n == 199:
        return 1.5 * xn(n) - 2 * xn(n-1) + 0.5 * xn(n-2)

xvalue = [xn(n) for n in nvalue]
yvalue = [yn(n) for n in nvalue]

plt.plot(nvalue, xvalue, 'm', label = 'Value of x(n)')
plt.plot(nvalue, yvalue, 'g', label = 'Value of y(n)')
plt.legend()
plt.show()