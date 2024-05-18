import matplotlib.pyplot as plt
import random
import math

class point:
    def __init__(self, dims):
        self.dims = [2*random.random()-1 for _ in range(dims)]  #1
    def e_dist(self, i=0):
        euc = lambda x, y : math.sqrt(math.pow(x,2)+math.pow(y,2))  #3
        def _e_dist(i=0):
            if 2 == len(self.dims[i:]):
                return euc(self.dims[i], self.dims[i+1])
            else:
                return euc(self.dims[i], _e_dist(i+1))
        return _e_dist()
        
def montecarlo(functions, dimensions, iterations):
    values = [functions(dimensions) for _ in range(iterations)]
    return values

def pi_calc(values):
    dimensions = len(values[0].dims)
    def _inside(value):
        if value > 1:
            return False
        else:
            return True
    inside = len(list(filter(_inside, [dist.e_dist() for dist in values]))) #2
    outside = len(values)
    return math.pow(math.pow(2, dimensions) * math.gamma(dimensions/2 + 1) * inside / outside ,2/dimensions)

n_2 = montecarlo(point, 2, 100000)
n_11 = montecarlo(point, 11, 100000)
print(pi_calc(n_2))
print(pi_calc(n_11))