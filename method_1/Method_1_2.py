import math as mt

def du(x):
    return (2 * mt.sin(x) ** 2) / 3 - (3 * mt.cos(x) ** 2) / 4

eps = 1/(10*10*10*10*10)

a = 0
b = mt.pi/2

while True:
    c = (a + b) / 2
    if du(c) * du(b) > 0:
        b = c
    else:
        a = c
    if b - a < eps:
        break
print(round(a,6))