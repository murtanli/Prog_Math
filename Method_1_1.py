import math as mt

def du(x):
    return x + mt.log(x + 0.5) + 0.5
eps = 1/(10*10*10*10*10)
a = 0
b = 2
while True:
    c = (a + b) / 2
    if du(c) * du(b) > 0:
        b = c
    else:
        a = c
    if b - a < eps:
        break
print(a)