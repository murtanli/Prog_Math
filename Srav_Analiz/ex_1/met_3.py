import math as mt



class met_3():
    def __init__(self,xn,eps):
        self.xn = xn
        self.eps = eps

    def mat(self):
        def fun(x):
            return mt.tan(x) - x

        def fun2(x):
            return (1/(mt.cos(x))**2) - 1


        while True:
            self.xn = self.xn - (fun(self.xn)/fun2(self.xn))
            if abs(fun(self.xn) / fun2(self.xn)) < self.eps:
                print(round(self.xn,6))
                break