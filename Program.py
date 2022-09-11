x = -3.2
mas = []

while x < 0:
    x = x + 0.2
    y = (0.7 * x ** 3) + (2 * x ** 2) - 1
    mas.append([x,round(y,2)])
f = open('C:\chisla.txt','w')
for ch in mas:
    f.write(str(ch) + "\n")
f.close()