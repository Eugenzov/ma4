import matplotlib.pyplot as plt
import random
import math

class pi_approx:
    def __init__(self) -> None:
        self.ycord = 2*random.random()-1
        self.xcord = 2*random.random()-1
        self.e_distance = lambda x, y : math.sqrt(math.pow(x,2)+math.pow(y,2))
    def euclid_distance(self):
        return self.e_distance(self.xcord, self.ycord)

def montecarlo(functions, iterations):
    values = [functions() for _ in range(iterations)]
    return values

def pi_calc(values):
    def _inside(value):
        if value > 1:
            return False
        else:
            return True
    inside = [dist.euclid_distance() for dist in values]
    inside = len(list(filter(_inside, inside)))
    outside = len(values) - inside
    
    return 4*inside/(outside+inside)

def main():
    n_1k = montecarlo(pi_approx, 1000)
    print(pi_calc(n_1k))
    n_10k = montecarlo(pi_approx, 10000)
    print(pi_calc(n_10k))
    n_100k = montecarlo(pi_approx, 100000)
    print(pi_calc(n_100k))
    for i in [n_1k, n_10k, n_100k]:
        xinside = []
        yinside = []
        xoutside = []
        youtside = []
        for j in i:
            if j.euclid_distance() > 1:
                xoutside.append(j.xcord)
                youtside.append(j.ycord)
            else:
                xinside.append(j.xcord)
                yinside.append(j.ycord)
        plt.scatter(xinside,yinside,color = "blue",label = "inside")
        plt.scatter(xoutside,youtside,color = "red",label = "outside")
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Monte Carlo Pi Approximation')
        plt.savefig(f'monte_carlo_pi_plot_{str(len(i))}.png')
        plt.clf()
    
main()