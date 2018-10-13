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
    def __init__(self, value):
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


class Matrix(object):
    def __init__(self, T, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[T.zero()] * cols for i in range(rows)]
    def __call__(self, data):
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] = data[i][j]
    def __str__(self):
        out = ''
        for i in range(self.rows):
            for j in range(self.cols):
                out += str(self.data[i][j]) + ' '
            out += '\n'
        return out

Space = Matrix(Z, 2, 2)
print(Space)

#A = Matrix()()
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

