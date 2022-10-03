import math as mt

def fun(x):
    return x**3 - 6*x**2 + 20

def fun2(x):
    return 3*x**2 -12*x

eps = 0.00001

xn = 2.31
i = 0
while True:
    xn = xn - (fun(xn)/fun2(xn))
    if abs(fun(xn) / fun2(xn)) < eps:
        print(round(xn,7))
        break