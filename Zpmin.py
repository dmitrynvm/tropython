import math


def convert(x, p):
	digits = []
	if x == 0: return [0]
	elif x == math.inf:
		return [math.inf]
	while x:
		digits.append(x % p)
		x = x // p
		digits.reverse()
	return digits


def nu(x, p):
    return int(str(math.ceil(math.log(x,p))),p)


class Zpmin(object):
    p = 10
    def __init__(self, value=math.inf):
        self.value = value
    def __add__(self, other):
        return Zpmin(min(self.value, other.value))
    def __mul__(self, other):
        return Zpmin(self.value * self.p**nu(other.value, self.p) + other.value)
    def __str__(self):
        out = ''
        #out += str(convert(self.value, self.p))
        out += str(self.value)
        return out


class Matrix(object):
    def __init__(self, rows=0, cols=0, data=[], algebra=Zpmin):
        self.rows = rows
        self.cols = cols
        if(data):
            self.data = data
        else:
            for i in range(rows):
                self.data.append([Zpmin()]*cols)
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

a = Zpmin(12)
b = Zpmin(3)
c = a * b
print('a =', c)
print('a =', c + a)
A = Matrix(2,2)
