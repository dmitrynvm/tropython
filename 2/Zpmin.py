import math

'''
def convert(x, p):
    digits = []
    if x == 0:
        return [0]
    elif x == math.inf:
		return math.inf
    while x:
		digits.append(x % p)
		x = x // p
		digits.reverse()
    return digits
'''


class Z(object):
    def __init__(self, value=math.inf):
        self.value = value
    def __add__(self, other):
        return Z(self.value + other.value)
    def __mul__(self, other):
        return Z(self.value * other.value)
    def __str__(self):
        return 'Z[' + str(self.value) + ']'
    @staticmethod
    def zero():
        return Z(0)
    @staticmethod
    def unit():
        return Z(1)

#Z.zero = def __call__(cls, *args, **kwds):
        print '__call__ of ', str(cls)
        print '__call__ *args=', str(args)
        return type.__call__(cls, *args, **kwds)Z(0)
#Z.unit = Z(1)


class Algebra(type):
    def __call__(cls, *args, **kwds):
        print('__call__ of ', str(cls))
        print('__call__ *args=', str(args))
        return type.__call__(cls, *args, **kwds)


class Matrix(object):
    __metaclass__ = Algebra
    def __init__(self):
        print('Object')
'''
    def __init__(self, rows=0, cols=0, data=[], algebra=Z):
        self.rows = rows
        self.cols = cols
        self.data = []
        if(data):
            self.data = data
        else:
            for i in range(rows):
                self.data.append([Z()]*cols)
    def __add__(self, other):
        res = Matrix(self.rows, self.cols)
        for i in range(res.rows):
            for j in range(res.cols):
                res.data[i][j] = other.data[i][j]
    def __str__(self):
        out = ''
        for i in range(res.rows):
            for j in range(res.cols):
                out += res.data[i][j] + ' '
            out << '\n'
        return out
'''

a = Z(12)
b = Z(3)
c = a * b
print('a + b =', a + b)
print('a * b =', a * b)
print('zero = ' + str(Z.zero()))
print('unit = ' + str(Z.unit()))
A = Matrix(2)
