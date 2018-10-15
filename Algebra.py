import math

oo = math.inf

def convert(x, p):
    digits = []
    out = ''
    if x == 0:
        return '0'
    elif x == math.inf:
        return 'oo'
    xx = x
    while xx:
        digits.append(x % p)
        xx = xx // p
        digits.reverse()
    out = ''.join([str(digit) for digit in digits])
    return out


class Semiring(object):

    def __init__(self):
        pass

    def __add__(self):
        pass

    def __mul__(self):
        pass

    @classmethod
    def __zero__(self):
        pass

    @classmethod
    def __unit__(self):
        pass


class Zp(object):
    p = 0
    def __init__(self, p=0):
        if p:
            Zp.p = p
        self.value = 0

    def __add__(self, other):
        res = Zp(self.p)
        res.value = self.value + other.value
        return res

    def __mul__(self, other):
        res = Zp(self.p)
        res.value = self.value * other.value
        return res

    def __repr__(self):
        return 'Z' + str(self.p) + '[' + str(self.value) + ']'

    def __str__(self):
        return str(self.value)

    def __call__(self, value):
        res = Zp(self.p)
        res.value = value
        return res

    def toLatex(self):
        return str(self)

class HMatrix(self, rows, cols, T, level);

class Matrix(object):
    def __init__(self, rows, cols, T, level):
        self.rows = rows
        self.cols = cols
        self.T = T
        self.level = level
        self.data = [[T] * cols for i in range(rows)]

    def __call__(self, data):
        res = Matrix(self.rows, self.cols, self.T, self.level)
        for i in range(self.rows):
            for j in range(self.cols):
                res.data[i][j] = self.T(data[i][j])
        return res

    def __str__(self):
        out = ''
        spaces = max([len(str(item)) for item in sum(self.data,[])])
        for i in range(self.rows):
            out += '|'
            for j in range(self.cols):
                padding = spaces
                if j != self.cols - 1:
                   padding += 1
                out += str(self.data[i][j]).ljust(padding)
            out += '|\n'
        return out

    def toLatex(self):
        file = open('sample.tex', 'w')
        out = ''
        if self.level == 2:
            fmt = '|'.join(['c'] * self.cols)
            out += '\\left(\\begin{array}{' + fmt + '}\n'
        else:
            out += '\t\\begin{matrix}\n'

        for i in range(self.rows):
            if self.level == 1:
                out += '\t\t'
            for j in range(self.cols):
                out += self[i,j].toLatex()
                if j != self.cols - 1:
                    if self.level == 2:
                        out += '\n\t&\n'
                    else:
                        out += ' & '
                else:
                    out += ' \\\\ '
            if self.level == 2 and i != self.rows - 1:
                out += '\\hline\n'
            else:
                out += '\n'

        if self.level == 2:
            out += '\\end{array}\\right)'
        else:
            out += '\t\\end{matrix}'
        file.write(out)
        return out

    def __getitem__(self, key):
        return self.data[key[0]][key[1]]

    def __setitem__(self, key, value):
        self.data[key[0]][key[1]] = value

    def __add__(self, other):
        res = Matrix(self.rows, self.cols, self.T, self.level)
        for i in range(res.rows):
            for j in range(res.cols):
                res[i,j] = self[i,j] + other[i,j]
        return res

    def __mul__(self, other):
        res = Matrix(self.rows, other.cols, self.T, self.level)
        for i in range(res.rows):
            for j in range(res.cols):
                for k in range(self.cols):
                    res[i,j] += self[i,k] * other[k,j]
        return res


if __name__ == '__main__':
    X = Matrix(2, 2, Zp(10), 1)
    M = Matrix(4, 4, X, 2)
    A01 = X([[1, 12], [0, 100]])
    A02 = X([[1, 13], [0, 100]])
    A10 = X([[1, 21], [0, 100]])
    A13 = X([[1, 24], [0, 100]])
    A20 = X([[1, 31], [0, 100]])
    A23 = X([[1, 34], [0, 100]])
    A31 = X([[1, 42], [0, 100]])
    A32 = X([[1, 43], [0, 100]])
    M[0,1] = A01
    M[0,2] = A02
    M[1,0] = A10
    M[1,3] = A13
    M[2,0] = A20
    M[2,3] = A23
    M[3,1] = A31
    M[3,2] = A32
    print((M*M).toLatex())
