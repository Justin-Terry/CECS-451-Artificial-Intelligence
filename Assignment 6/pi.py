import random
import math

class Pi:
    def __init__(self, exp):
        self.exp = exp
        self.pi = 0

    def simulation(self):
        numInCirc = 0
        numOfTrys = 10 ** self.exp

        for i in range(numOfTrys):
            x = random.random()
            y = random.random()
            d = x ** 2 + y ** 2
            if d < 1.0:
                numInCirc += 1
        self.pi = numInCirc / numOfTrys * 4

    def print(self):
        print('n = 10 ^', self.exp, '\tpi =', "{0:.6f}".format(self.pi), '\terror =', "{0:.4f}".format(abs((self.pi - math.pi) * 100)))


if __name__ == '__main__':
    for i in range(4):
        driver = Pi(i+3)
        driver.simulation()
        driver.print()