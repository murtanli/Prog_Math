import math as mt
eps = 0.00001
xn = 0
xk = 2

class met_2():
    def __init__(self,xn,xk,eps):
        self.xn = xn
        self.xk = xk
        self.eps = eps



    def mat(self):
        def fun1(x):
            #return x + mt.log(x + 0.5) + 0.5
            return x ** 3 - 3 * x - 5
        while True:
            p = (fun1(self.xk)*self.xn-fun1(self.xn)*self.xk)/(fun1(self.xk) - fun1(self.xn))
            if abs(fun1(p)) <= self.eps:
                break

            if fun1(self.xn)*fun1(self.xk) > 0:
                self.xn = p
            else:
                self.xk = p
            if abs((fun1(self.xk) * self.xn - fun1(self.xn) * self.xk) / fun1(self.xk) - fun1(self.xn) - p) <= self.eps:
                break
        print(round(p, 6))




