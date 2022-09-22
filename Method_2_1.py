import math as mt
import matplotlib.pyplot as plt

fig = plt.figure()

def fun1(x):
    return x + mt.log(x + 0.5) + 0.5

eps = 0.00001

xn = 0
xk = 2

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




