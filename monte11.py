import matplotlib.pyplot as plt
import random
import math

class pi_approx:
    def __init__(self) -> None:
        self.ycord = 2*random.random()-1
        self.xcord = 2*random.random()-1
    def euclid_distance(self):
        return math.sqrt(math.pow(self.xcord,2) + math.pow(self.ycord,2))

def montecarlo(functions, iterations):
    values = []
    for i in range(iterations):
        values.append(functions())
    return values

def pi_calc(values):
    inside = 0
    outside = 0
    for i in values:
        if i.euclid_distance() > 1:
            outside += 1
        else:
            inside += 1
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