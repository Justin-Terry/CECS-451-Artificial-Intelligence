from tabulate import tabulate

class Gibbs:

    def __init__(self):
        self.transition = [["S1", .34485,     .5,     .15515,     0],
                           ["S2", 0,          .5626,  0,          .4374],
                           ["S3", .34485,     0,      .15515,     .5],
                           ["S4", 0,          .0626,  0,          .9374]]
        self.partA()
        self.partB()

    def partA(self):
        print("P(C|-s,r) = <0.8748, 0.1252>")
        print("P(C|-s,-r) = <0.3103, 0.6897>")
        print("P(R|c,-s,w) = <1,0>")
        print("P(R|-c,-s,w) = <1,0>")

    def partB(self):
        print(tabulate(self.transition, ["S1", "S2", "S3", "S4"], tablefmt="simple"))

if __name__ == '__main__':
    driver = Gibbs()