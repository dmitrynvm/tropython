import math

def nu(x, p):
    return int(str(math.ceil(math.log(x,p))),p)

class Zpmin(object):
    p = 4
    def __init__(self, value):
        self.value = value
    def __add__(self, other):
        return Zpmin(self.value * self.p**nu(other.value, self.p) + other.value)
    def __mul__(self, other):
        return Zpmin(min(self.value, other.value))
    def __str__(self):
        out = ''
        out += str(int(str(self.value), self.p))
        return out

a = Zpmin(12)
b = Zpmin(3)
c = a + b
print('a =', c)
