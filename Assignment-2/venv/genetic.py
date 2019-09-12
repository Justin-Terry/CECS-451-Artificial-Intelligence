# Justin Terry
# CECS 451 A.I.
# 9/12/2019

from board import Board
import random

class Genetic:
    def __init__(self):
        self.no_boards = 0
        self.max_steps = 0
        self.num_queens = 0;
        self.no_steps = 1
        self.boards = []

    def setup(self):
        num_boards = 3
        while(num_boards % 2 != 0):
            num_boards = int(input("How many boards would you like to use (even number)?:"))
            if(num_boards %2 != 0):
                print("The number of boards must be even.")
        max_tries = int(input("What is the maximum number of steps you're willing to take?: "))
        num_queens = 0
        while (num_queens <= 3):
            num_queens = int(input("How many queens would you like to place? (Must be greater than 3)?:"))
            if (num_queens <= 3):
                print("That is impossible.")
        self.no_boards = num_boards
        self.max_steps = max_tries
        self.num_queens = num_queens
        self.create_boards()

    def find_a_solution(self):
        while (self.no_steps < self.max_steps):
            print("Step #" + str(self.no_steps))
            self.show_boards()
            self.show_fitness()
            self.set_fitness()
            self.show_states()
            self.genetic_algorithm()
            self.no_steps += 1
            print("\n")
        print("No solution after", max_steps,"steps.")

    def create_boards(self):
        for i in range(0, self.no_boards):
            newBoard = Board(self.num_queens)
            newBoard.set_queens()
            self.boards.insert(i, newBoard)

    def show_boards(self):
        for i in range(0, self.num_queens):
            for board in self.boards:
                print(str(board.getMap()[i]).replace(",", ""), end="    ")
            print()

    def set_fitness(self):
        for board in self.boards:
            board.genetic_fitness()

    def show_fitness(self):
        for board in self.boards:
            board.genetic_fitness()
            fitness_string = "Fitness: " + str(board.fit)
            print(fitness_string.ljust(int(self.num_queens * 2)+5), end="")
        print()

    def show_states(self):
        for board in self.boards:
            board_string = "State: " + board.get_state()
            print(board_string.ljust(int(self.num_queens * 2)+5), end="")
        print()

    def genetic_algorithm(self):
        # Get the fitness values for each of the boards.
        fitness_values, fitness_total = self.get_fitness_values()
        # Convert the fitness values to percentage values
        fitness_values = self.map_fitness_to_percent(fitness_values, fitness_total)
        # Perform selection to get new states, second param of function is the eliteism scalar
        new_states = self.selection(fitness_values, 100)
        # Perform crossover
        crossed_over_states = self.perform_crossover(new_states)
        # Perform mutation
        mutated_states = self.perform_mutation(crossed_over_states)
        # Set the boards to the mutated states
        self.set_states(mutated_states)

    def finished(self):
        print("Finished in", self.no_steps, "steps.")

    def set_states(self, states):
        for i in range(0, len(self.boards)):
            self.boards[i].set_state(states[i])

    def perform_crossover(self, states):
        children_states = []
        # Generate a sample the size of states of index values
        cross_over_state_indexes = random.sample(range(0, self.num_queens), int(len(states)/2))

        for i in range(0, int(len(states)/2)):
            # Generate a random index to crossover at
            mutation_index = random.randint(0, self.num_queens-1)
            # Perform crossovers
            children_states.append(states[i][:mutation_index] + states[int(i+len(states)/2)][mutation_index:])
            children_states.append(states[int(i+len(states)/2)][:mutation_index] + states[i][mutation_index:])
        return children_states

    def perform_mutation(self, states):
        mutated_states = []
        for state in states:
            # Generate a random index to mutate for this state
            index_to_mutate = random.randint(0,self.num_queens-1)
            arr = list(state)
            arr[index_to_mutate] = random.randint(0,self.num_queens-1) # Perform the mutation
            mutated_states.append("".join(str(x) for x in arr))
        return mutated_states


    def selection(self, fitness_values, eliteism):
        new_states = []
        maxIndex = fitness_values.index(max(fitness_values))
        new_states.insert(maxIndex, self.boards[maxIndex].get_state())
        # fitness_values[maxIndex] = fitness_values[maxIndex]*eliteism
        for i in range(0,self.no_boards):
            if i is not maxIndex:
                selector = random.uniform(0, fitness_values[maxIndex])
                if selector > 0 and selector < fitness_values[0]:
                    new_states.insert(i, self.boards[0].get_state())
                elif selector > fitness_values[0] and selector < fitness_values[0] + fitness_values[1]:
                    new_states.insert(i, self.boards[1].get_state())
                elif selector > fitness_values[0] + fitness_values[1] and selector < fitness_values[0] + fitness_values[
                    1] + fitness_values[2]:
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
            if(fitness_values[i] == self.boards[i].max_fit):
                self.finished()
                exit();
        return fitness_values, fitness_total

    def map_fitness_to_percent(self, fitness_values, fitness_total):
        for i in range(0, self.no_boards):
            temp = fitness_values[i]
            fitness_values[i] = temp/fitness_total
        return fitness_values


if __name__ == '__main__':
    # Run genetic
    gene = Genetic()
    gene.setup()
    gene.find_a_solution()
