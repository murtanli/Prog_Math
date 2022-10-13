from met_1 import met_1
from met_2 import met_2
from met_3 import met_3

#Метод 1
a = 1.9
b = 2.93
eps = 0.000001
num = met_1(a,b,eps)
print('Метод 1')
num.mat()


#Метод 2
eps = 0.000001
xn = 1.9
xk = 2.93

num2 = met_2(xn,xk,eps)
print('Метод 2')
num2.mat()

#Метод 3

eps = 0.00001
xn = 1.9

num3 = met_3(xn,eps)
print('Метод 2')
num3.mat()