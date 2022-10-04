import math as mt
class met_1:
    def __init__(self,a,b,eps):
        self.a = a
        self.b = b
        self.eps = eps
    def du(x):
        return x + mt.log(x + 0.5) + 0.5
    def mat(self):
        while True:
            c = (self.a + self.b) / 2
            if self.du(c) * self.du(b) > 0:
                b = c
            else:
                a = c
            if b - a < self.eps:
                break
        print(a)
