import random
import numpy as np


class Board:
    def __init__(self, n):
        self.n_queen = n
        self.map = [[0 for j in range(n)] for i in range(n)]
        self.fit = n * (n-1) // 2
        self.max_fit = n * ((n-1)/2)


    def set_queens(self):
        for i in range(self.n_queen):
            j = random.randint(0, self.n_queen - 1)
            self.map[i][j] = 1

    def get_max_fit(self):
        return self.max_fit

    def set_state(self, state):
        self.map = [[0 for j in range(self.n_queen)] for i in range(self.n_queen)]
        for i in range(0, self.n_queen):
            self.map[i][int(state[i])] = 1;

    def get_state(self):
        state = ""
        for r in range(0, self.n_queen):
            for c in range(0, self.n_queen):
                if self.map[r][c] == 1:
                    state += (str(c))
        return state

    def show(self):
        print(np.matrix(self.map))

    def getMap(self):
        return self.map

    def genetic_fitness(self):
        self.fit = self.n_queen * (self.n_queen - 1) // 2
        for i in range(self.n_queen):
            for j in range(self.n_queen):
                if self.map[i][j] == 1:
                    for k in range(1, self.n_queen - i):
                        if self.map[i + k][j] == 1:
                            self.fit -= 1
                        if j - k >= 0 and self.map[i + k][j - k] == 1:
                            self.fit -= 1
                        if j + k < self.n_queen and self.map[i + k][j + k] == 1:
                            self.fit -= 1

    def fitness(self):
        self.fit = self.n_queen * (self.n_queen - 1) // 2
        for i in range(self.n_queen):
            for j in range(self.n_queen):
                if self.map[i][j] == 1:
                    for k in range(1, self.n_queen - i):
                        if self.map[i + k][j] == 1:
                            self.fit -= 1
                        if j - k >= 0 and self.map[i + k][j - k] == 1:
                            self.fit -= 1
                        if j + k < self.n_queen and self.map[i + k][j + k] == 1:
                            self.fit -= 1


if __name__ == '__main__':
    test = Board(5)
    test.set_queens()
    test.show()

