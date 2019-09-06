import random
import numpy as np


class Board:
    def __init__(self, n):
        self.n_queen = n
        self.map = [[0 for j in range(n)] for i in range(n)]

    def set_queens(self):
        count = self.n_queen
        while count > 0:
            x = random.randint(0, self.n_queen ** 2 - 1)
            i = x // self.n_queen
            j = x - i * self.n_queen
            if self.map[i][j] != 1:
                self.map[i][j] = 1
                count -= 1

    def show(self):
        print(np.matrix(self.map))


if __name__ == '__main__':
    test = Board(5)
    test.set_queens()
    test.show()

