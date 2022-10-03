import math as mt

def fun(x):
    return mt.tan(x) - x

def fun2(x):
    return (1/(mt.cos(x))**2) - 1

eps = 0.00001

xn = 4.67
i = 0
while True:
    xn = xn - (fun(xn)/fun2(xn))
    if abs(fun(xn) / fun2(xn)) < eps:
        print(round(xn,7))
        break