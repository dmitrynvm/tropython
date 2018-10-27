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

'''
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
'''


Z = int

def Add(left, right):
    result = Matrix(left.size, left.algebra)
    for i in range(result.rows):
        for j in range(result.cols):
            result[i,j] = left[i,j] + right[i,j]
    return result

def Min(left, right):
    result = Matrix(left.size, left.algebra)
    for i in range(result.rows):
        for j in range(result.cols):
            result[i,j] = min(left[i,j], right[i,j])
    return result

def Mul(left, right):
    result = Matrix((left.rows, right.cols), left.algebra)
    for i in range(result.rows):
        for j in range(result.cols):
            for k in range(left.cols):
                result[i,j] += left[i,k] * right[k,j]
    return result


def Zero(matrix):
    for i in range(matrix.rows):
        for j in range(matrix.cols):
            matrix[i,j] = 0
    return matrix

def Unit(matrix):
    for i in range(matrix.rows):
        for j in range(matrix.cols):
            if i == j:
                matrix[i,j] = 1
            else:
                matrix[i,j] = 0
    return matrix


class Matrix(object):
    def __init__(self, size, algebra):
        self.size = size
        self.algebra = algebra
        self.data = [[algebra.type] * size[1] for i in range(size[1])]

    def __getitem__(self, key):
        return self.data[key[0]][key[1]]

    def __setitem__(self, key, value):
        self.data[key[0]][key[1]] = value

    def __getattr__(self, name):
        if name == 'rows':
            return self.size[0]
        elif name == 'cols':
            return self.size[1]
        else:
            return self.algebra.get(name, None)

    def __add__(self, other):
        return self.algebra.add(self, other)

    def __mul__(self, other):
        return self.algebra.mul(self, other)

    def __call__(self, data):
        result = self.clone()
        for i in range(self.rows):
           for j in range(self.cols):
               result[i,j] = data[i][j]
        return result

    def __str__(self):
        out = ''
        if self.type == int:
            spaces = max([len(str(item)) for item in sum(self.data,[])])
            for i in range(self.rows):
                out += '|'
                for j in range(self.cols):
                    padding = spaces
                    if j != self.cols - 1:
                        padding += 1
                    out += str(self.data[i][j]).ljust(padding)
                out += '|\n'
        else:
            for i in range(self.rows):
                out += '\n|\n'
                for j in range(self.cols):
                    out += str(self.data[i][j])
                    if j != self.cols - 1:
                        out += '\n'
                out += '|\n'
        return out

    def clone(self):
        return Matrix(self.size, self.algebra)


class Algebra(dict):
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__


MZPlusMult = Algebra({
    'type': Z,
    'add': Add,
    'mul': Mul,
    'zero': Zero,
    'unit': Unit
})

MMZPlusMult = Algebra({
    'type': MZPlusMult,
    'add': Add,
    'mul': Mul,
    'zero': Zero,
    'unit': Unit
})

X = Matrix((2,2), MZPlusMult)
M = Matrix((4,4), MMZPlusMult)

A = X([[1,-20], [-30,4]])
B = X([[5,6], [7,8]])
print(Min(A,B))
print(M)

'''
    def __call__(self, data):
        res = Matrix(self.rows, self.cols, self.algebra)
        for i in range(self.rows):
            for j in range(self.cols):
                res.data[i][j] = self.T(data[i][j])
        return res


    def __add__(self, other):
        res = Matrix(self.rows, self.cols, self.T)
        for i in range(res.rows):
            for j in range(res.cols):
                res[i,j] = self[i,j] + other[i,j]
        return res

    def __mul__(self, other):
        res = Matrix(self.rows, other.cols, self.T)
        for i in range(res.rows):
            for j in range(res.cols):
                for k in range(self.cols):
                    res[i,j] += self[i,k] * other[k,j]
        return res


'''


'''
X = Matrix(2, 2, Z)
M = Matrix(4, 4, X)
A12 = X([[1, 12], [0, 100]])
A13 = X([[1, 13], [0, 100]])
A21 = X([[1, 21], [0, 100]])
A24 = X([[1, 24], [0, 100]])
A31 = X([[1, 31], [0, 100]])
A33 = X([[1, 34], [0, 100]])
A41 = X([[1, 42], [0, 100]])
A42 = X([[1, 43], [0, 100]])
M[0,1] = A12
M[0,2] = A13
M[1,0] = A21
M[1,3] = A24
M[2,0] = A31
M[2,3] = A
M[3,1] = A
M[3,2] = A
print(M)
'''

'''

if __name__ == '__main__':
    E = Matrix(2, 2, Zp(10))
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
'''
