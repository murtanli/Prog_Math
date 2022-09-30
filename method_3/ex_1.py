import math as mt
def fun(x):
    return mt.tan(x) - x
def fun2(x):
    return (1/(mt.cos(x))**2) - 1
eps = 1/10*10*10*10*10

xn = 4.67

while True:
    xn = xn - (fun(xn)/fun2(xn))
    if abs(xn - fun(xn)) < eps:
        print(xn)
        break