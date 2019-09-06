from board import Board


class Genetic:
    def __init__(self):
        self.no_steps = 0


if __name__ == '__main__':
    brd = Board(5)
    brd.set_queens()
    brd.show()
