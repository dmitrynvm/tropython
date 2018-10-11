from itertools import permutations

class Grid(object):
    def __init__(self, p=0, q=0, data=[], sizes=()):
        self.p = p
        self.q = q
        
        if data:
            self.data = data
        else:
            self.data = [0] * p
            for i in range(self.q):
                self.data[i] = i + 1

        if sizes:
            self.sizes = sizes
            self.p = 1
            for size in sizes:
                self.p *= size
        else:
            self.sizes = ()
        self.count = 0
        self.perms = list(permutations(self.data))
        self.iters = len(self.perms)

        
    def __iter__(self):
        return self

    def __str__(self):
        out = ''
        index = 0
        if self.sizes:
            for i in range(self.sizes[0]):
                for j in range(self.sizes[1]):
                    out += '|' + str(self.data[index])
                    index += 1
                out += '|\n'
        return out

    def __next__(self):
        if self.count >= self.iters:
            raise StopIteration()
        perm = self.perms[self.count]
        self.count += 1
        return Grid(p=self.p, q=self.q, data=perm, sizes=self.sizes)
        
grid = Grid(p=4,q=4,sizes=(2,2))
for idx, val in enumerate(grid):
  print(idx+1)
  print(val)
