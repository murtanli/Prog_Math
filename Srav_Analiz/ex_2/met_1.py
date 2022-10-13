import math as mt

class met_1():
    def __init__(self,a,b,eps):
        self.a = a
        self.b = b
        self.eps = eps

    def mat(self):
        def du(x):
            #return x + mt.log(x + 0.5) + 0.5
            return x**3 - 3 * x - 5

        while True:
            c = (self.a + self.b) / 2
            if du(c) * du(self.b) > 0:
                self.b = c
            else:
                self.a = c
            if self.b - self.a < self.eps:
                break

        print(round(self.a,6))
