import random
import numpy as np


class Board:
    def __init__(self, n):
        self.n_queen = n
        self.map = [[0 for j in range(n)] for i in range(n)]

    def set_queens(self):
        for i in range(self.n_queen):
            j = random.randint(0, self.n_queen - 1)
            self.map[i][j] = 1

    def show(self):
        print(np.matrix(self.map))

    def getMap(self):
        return self.map


if __name__ == '__main__':
    test = Board(5)
    test.set_queens()
    test.show()

