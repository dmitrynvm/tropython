import math


class Qpmin:
	def __init__(self, value = 0, p = 10):
		self.value = value
		self.p = p
		self.coefs = int2list(value, p)
	
	def __repr__(self):
		'Representation.'
		out = ''
		n = len(self.coefs)
		for i in range(n):
			out += str(self.coefs[i]) + '*' + str(self.p) + '^' + str(i)
			if i != n-1:
				out += ' + '
		return out

	def __add__(self, other):
		'+ operator.'
		return Qpmin(max(self.value, other.value), self.p)

	def __mul__(self, other):
		'* operator.'
		return Qpmin(self.value + other.value, self.p)

	def __truediv__(self, other):
		'/ operator.'
		return Qpmin(self.value - other.value, self.p)

	def __eq__(self, other):
		'== operator.'
		if isinstance(other, Qpmin):
			return self.value == other.value
		else:
			return self.value == other


Qpmin.zero = Qpmin(math.inf)
Qpmin.unit = Qpmin(0)

