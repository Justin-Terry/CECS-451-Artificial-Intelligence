#tabulate is used for outputing partB
from tabulate import tabulate
import random

class Gibbs:

    def __init__(self):
        self.transition = [["S1", .34485,     .5,     .15515,     0],
                           ["S2", 0,          .5626,  0,          .4374],
                           ["S3", .34485,     0,      .15515,     .5],
                           ["S4", 0,          .0626,  0,          .9374]]
        self.partA()
        self.partB()
        self.performMCMC()

    def partA(self):
        print("P(C|-s,r) = <0.8748, 0.1252>")
        print("P(C|-s,-r) = <0.3103, 0.6897>")
        print("P(R|c,-s,w) = <1,0>")
        print("P(R|-c,-s,w) = <1,0>")

    def partB(self):
        print(tabulate(self.transition, ["S1", "S2", "S3", "S4"], tablefmt="simple"))

    def createRandomState(self):
        state = []
        c = random.randint(0,1)
        state.append(c)
        state.append(self.generateRandomR(c))
        state.append(self.generateRandomS(c))
        state.append(self.generateRandomW(state[1], state[2]))
        return state

    def generateRandomR(self, C):
        ran = random.random()
        if(C == 1):
            if(ran >= .2):
                return 1
            else:
                return 0
        else:
            if(ran >= .8):
                return 1
            else:
                return 0

    def generateRandomS(self, C):
        ran = random.random()
        if(C == 1):
            if(ran >= .9):
                return 1
            else:
                return 0
        else:
            if(ran >= .5):
                return 1
            else:
                return 0

    def generateRandomW(self, R, S):
        ran = random.random()
        if(R == 1 and S == 1):
            #r,s
            if(ran >= .99):
                return 0
            else:
                return 1
        if(R == 1 and S == 0):
            #r, -s
            if(ran >= .9):
                return 0
            else:
                return 1
        if(R == 0 and S == 1):
            #-r, s
            if(ran >= .9):
                return 0
            else:
                return 1
        if(R == 0 and S == 0):
            #-r, -s
            return 0



    def performMCMC(self):
        numOfNotC = 0
        numOfC = 0
        numOfRuns = 0
        for i in range(1000000):
            state = self.createRandomState()
            if(state[0] == 0 and state[2] == 0 and state[3] == 1):
                numOfNotC += 1
                numOfRuns += 1
            elif (state[0] == 1 and state[2] == 0 and state[3] == 1):
                numOfC += 1
                numOfRuns += 1

        print("<", numOfC/numOfRuns, ",", numOfNotC/numOfRuns, ">")


if __name__ == '__main__':
    driver = Gibbs()