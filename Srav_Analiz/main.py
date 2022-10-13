from met_1 import met_1
from met_2 import met_2
from met_3 import met_3

#Метод 1

a = 0
b = 2
eps = 0.000001
num = met_1(a,b,eps)
num.mat()


#Метод 2
eps = 0.000001
xn = 0
xk = 2

num2 = met_2(xn,xk,eps)
num2.mat()

#Метод 3

eps = 0.00001
xn = 4.67

num3 = met_3(xn,eps)
num3.mat()