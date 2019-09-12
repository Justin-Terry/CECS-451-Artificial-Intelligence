# Justin Terry
# CECS 451 A.I.
# 9/12/2019
from board import Board

class Hill_Climb:
    def __init__(self):
        self.no_steps = 0

    def setup(self):
        self.board = Board(int(input("How many queens to set?: ")))
        self.stuck_at = int(input("Try a random restart if stuck after how many tries?: "))
        self.board.set_queens()
        self.board.show()


    def climb_hill(self):
        # Until a solution is found continue to manipulate the positions of the queens, if it gets stuck on a board
        # try a random resart and continue.
        num_searches = 0
        while(True):
            if num_searches > self.stuck_at:
                print("\nStuck after", self.stuck_at,"tries, trying random board.")
                self.board = Board(8)
                self.board.set_queens()
                num_searches = 0
            else:
                num_searches += 1
            self.search_board()

    # search_board uses the state of the board to change the position, in the row, of each queen to the position
    # with the highest fitness value. If that fitness value is the max possible for the board it exits.
    def search_board(self):
        current_state = self.board.get_state()
        self.board.fitness()
        current_fitness = self.board.fit
        best_state = self.board.get_state()

        for i in range(0, len(current_state)):
            next_state = best_state
            self.no_steps += 1
            for j in range(0, self.board.n_queen):
                next_state = "".join((next_state[:i], str(j), next_state[i + 1:]))
                self.board.set_state(next_state)
                self.board.fitness()
                if (self.board.fit == self.board.get_max_fit()):
                    print("\nSolution board found! Fitness:", self.board.fit)
                    self.board.show()
                    self.finished();
                if (self.board.fit > current_fitness):
                    current_fitness = self.board.fit
                    best_state = next_state
                    print("\nBetter position selected, fitness:", self.board.fit)

    def finished(self):
        print("Finished in", self.no_steps, "steps.")
        exit()


if __name__ == '__main__':
    hc = Hill_Climb()
    hc.setup()
    hc.climb_hill()


