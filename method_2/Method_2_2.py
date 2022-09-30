import math as mt

def fun1(x):
    return (x**4) + (2*x)**3 - x - 1

eps = 0.00001

xn = 0.1
xk = 1

while True:
    p = (fun1(xk)*xn-fun1(xn)*xk)/(fun1(xk) - fun1(xn))
    if abs(fun1(p)) <= eps:
        break

    if fun1(xn)*fun1(xk) > 0:
        xn = p
    else:
        xk = p
    if abs((fun1(xk) * xn - fun1(xn) * xk) / fun1(xk) - fun1(xn) - p) <= eps:
        break

print('x=', round(p, 6))




