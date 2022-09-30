import math as mt

def fun(x):
    return mt.tan(x) - x

eps = 1/10*10*10*10*10

x1 = 4.67
while True:
    x0 = x1
    x1 = x0-fun(x0) / fun(x0)

    if abs(x0 - x1) <= eps:
        print(x1,fun(x1))
        break

