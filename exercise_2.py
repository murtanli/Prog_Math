from sympy import *
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()

mas = []
lines = 0
x = []
y = []
with open(r'C:\Users\amirm\OneDrive\Рабочий стол\Project\chisla.txt','r') as f:
    lines = 0
    for line in f:
        lines += 1
        if lines % 2:
            x.append(line.strip('\n'))
        else:
            y.append(line.strip('\n'))

for num in x:
    x2 = Symbol('x')
    y2 = (0.7 * x2 ** 3) + (2 * x2 ** 2) - 1
    p = y2.diff(x2)
    res = solve(Eq(y2,0))

mas2 = []
for n in res:
    i4 = 0
    r = ''
    for n2 in str(n):
        i4 += 1
        if i4 < 16:
            r = r + n2
    mas.append(float(r))
y6 = [0,0,0]
print(mas)
plt.scatter(mas,y6)
plt.show()