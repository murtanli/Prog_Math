import matplotlib.pyplot as plt
fig = plt.figure()

x = -3.2
mas = []
while x < 0:
    x = x + 0.2
    y = (0.7 * x ** 3) + (2 * x ** 2) - 1
    mas.append(["%.2f" % round(x,2),"%.2f" % round(y,2)])
    plt.scatter(x,y)
x = []
y = []
for i in range(len(mas)):
    k = 0
    pp = ''
    for num in mas[i]:
        k += 1
        if k == 1:
            x.append(float(num))
        else:
            y.append(float(num))
plt.plot(x,y)
plt.savefig('pic_11_1_2.png')
plt.show()
