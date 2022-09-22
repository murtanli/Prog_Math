import math as mt
import matplotlib.pyplot as plt

fig = plt.figure()

def fun1(x):
    return x + mt.log10(x + 0.5) + 0.5

eps = 0.00001

xn = 0
xk = 2
while True:
    p = (fun1(xk)*xn-fun1(xn)*xk)/(fun1(xk)-fun1(xn))
    if abs(fun1(p)) <= eps:
        print('x=',p)
        break

    if fun1(xn)*fun1(xk) > 0:
        xn = p
    else:
        xk = p
    if abs((fun1(xk) * xn - fun1(xn) * xk) / fun1(xk) - fun1(xn) - p) <= eps:
        break
print('x=', p)



"""eps = 1/(10*10*10*10*10)
x2 = []
y2 = []
for i in range(3):
    y = fun(i)
    x2.append(i)
    y2.append(y)
plt.plot(x2,y2)
plt.show()
a = 0
b = 2"""
