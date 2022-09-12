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
    #plt.scatter(res,0)
    print(res)
plt.show()