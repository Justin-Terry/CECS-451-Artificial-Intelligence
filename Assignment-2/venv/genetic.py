from board import Board

# Maximum non-attacking pairs is 30

class Genetic:
    def __init__(self):
        self.no_steps = 0
        self.board = Board(5)
        self.board.set_queens()
        self.board.show()
        self.calculateH()
        exit()

    # Returns the state in format x1 y1 x2 y2 x3 y3 etc with no spaces
    def getState(self):
        state = ""
        for r in range(0, 5):
            for c in range(0, 5):
                if self.board.getMap()[r][c] == 1:
                    state += (str(c))
        return state

    def calculateH(self):
        state = self.getState()
        totalAttackingPairs = 0
        for i in range(0,5):
            totalAttackingPairs += self.checkDiagnol(int(i), "03142")
            totalAttackingPairs += self.checkColumn(int(i), "03142")
        print(totalAttackingPairs)

    # Checks all the columns for the row, r, given
    def checkColumn(self, r, state):
        row = int(r)
        rowValue =int(state[row])
        nonAttacking = 0
        conflicts = 0
        for currRow in range(0, len(state)):
            if(currRow != row):
                if(int(state[currRow]) != rowValue):
                    nonAttacking+=1
                else:
                    conflicts += 1
        print("Column Conflicts: ", conflicts)
        return nonAttacking

    def checkDiagnol(self, r, state):
        print("Checking row: ", r)
        row = int(r)
        rowValue = int(state[row])
        conflicts = 0
        nonAttacking = 0
        tempRow = int(row - 1);
        tempColumn = int(rowValue - 1)
        while(tempRow >= 0 and tempColumn >= 0):
            print("Against: row: ", tempRow, " column: ", tempColumn)
            if(int(state[tempRow]) == tempColumn):
                print(tempRow, " has a diag conflict")
                conflicts+=1
            tempRow-=1
            tempColumn-=1
        tempRow = int(row + 1)
        tempColumn = int(rowValue + 1)
        while(tempRow < 5 and tempColumn < 5):
            print("Against: row: ", tempRow, " column: ", tempColumn)
            if(int(state[tempRow]) == tempColumn):
                print(tempRow, " has a diag conflict")
                conflicts+=1
            tempRow+=1
            tempColumn+=1
        if(conflicts == 0):
            nonAttacking += 2

        print("Diag Conflicts: ", conflicts)
        return nonAttacking

# if __name__ == '__main__':
#     brd = Board(5)
#     brd.set_queens()
