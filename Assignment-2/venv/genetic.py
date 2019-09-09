from board import Board
import random
# Maximum non-attacking pairs is 10

class Genetic:
    def __init__(self):
        self.no_boards = 10
        self.no_steps = 1
        self.boards = []
        self.create_boards()

        while(True):
            print("Step #" + str(self.no_steps))
            self.show_boards()
            self.show_fitness()
            self.show_states()
            self.perform_swap()
            self.no_steps += 1
            print("\n\n")
        exit()

    def create_boards(self):
        for i in range(0, self.no_boards):
            newBoard = Board(5)
            newBoard.set_queens()
            self.boards.insert(i, newBoard)

    def show_boards(self):
        for i in range(0, 5):
            for board in self.boards:
                print(str(board.getMap()[i]).replace(",", ""), end="    ")
            print()

    def show_fitness(self):
        for board in self.boards:
            board.genetic_fitness()
            print("Fitness:",board.fit, "    ", end="")
        print()

    def show_states(self):
        for board in self.boards:
            print("State:",board.get_state(),"  ", end="")
        print()

    def perform_swap(self):
        fitness_values, fitness_total = self.get_fitness_values()

        fitness_values = self.map_fitness_to_percent(fitness_values, fitness_total)

        new_states = self.generate_selection(fitness_values)

        options = random.sample(range(0,self.no_boards), self.no_boards)
        splits = []
        for i in range(0, int(self.no_boards/2)):
            splits.insert(i, random.uniform(0, int(self.no_boards/2)))

        mutated_states = self.perform_crossover(new_states, options, splits)

        for i in range(0, len(self.boards)):
            self.boards[i].set_state(mutated_states[i])

    def finished(self):
        print("Finished in", self.no_steps, "steps.")

    def perform_crossover(self, states, options, splits):
        print(options)
        split = 0
        for i in range(0,len(states),2):
            state1 = states[options[i]]
            state2 = states[options[i+1]]
            states[options[i]] = state1[0:int(splits[split])] + state2[int(splits[split]):len(state2)]
            states[options[i+1]] = state2[0:int(splits[split])] + state1[int(splits[split]):int(len(state2))]
            split+=1

        indexes = random.sample(range(0,self.no_boards-1), self.no_boards-1)
        print("Indexes:", indexes)
        print("States:", states)
        for i in range(0, self.no_boards-1):
            s = states[indexes[i]]
            print("State:", s, "Index:", indexes[i])
            char = str(random.randint(0,4))
            print("c:",char)
            s = s[0:indexes[i]] + char + s[indexes[i]+1:]
            states[indexes[i]] = s
            print("New State:", s)

        return states

    def generate_selection(self, fitness_values):
        new_states = []
        maxIndex = fitness_values.index(max(fitness_values))
        fitness_values[maxIndex] = fitness_values[maxIndex]*100
        for i in range(0,self.no_boards):
            selector = random.uniform(0,fitness_values[maxIndex])
            if selector > 0 and selector < fitness_values[0]:
                new_states.insert(i, self.boards[0].get_state())
            elif selector > fitness_values[0] and selector < fitness_values[0] + fitness_values[1]:
                new_states.insert(i, self.boards[1].get_state())
            elif selector > fitness_values[0] + fitness_values[1] and selector < fitness_values[0] + fitness_values[1] + fitness_values[2]:
                new_states.insert(i, self.boards[2].get_state())
            else:
                new_states.insert(i, self.boards[3].get_state())
        return new_states

    def get_fitness_values(self):
        fitness_values = []
        fitness_total = 0

        for i in range(0, self.no_boards):
            fitness_values.insert(i, self.boards[i].fit)
            fitness_total += self.boards[i].fit
            if(fitness_values[i] == 10):
                self.finished()
                exit();
        return fitness_values, fitness_total

    def map_fitness_to_percent(self, fitness_values, fitness_total):
        for i in range(0, self.no_boards):
            temp = fitness_values[i]
            fitness_values[i] = temp/fitness_total
        return fitness_values


# if __name__ == '__main__':
#     brd = Board(5)
#     brd.set_queens()
