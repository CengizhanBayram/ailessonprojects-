from simpleai.search import SearchProblem
from simpleai.search import breadth_first
from simpleai.search import depth_first
from simpleai.search import uniform_cost
from simpleai.search import greedy
from simpleai.search import astar
from simpleai.search import iterative_limited_depth_first
from simpleai.search import limited_depth_first
from simpleai.search import hill_climbing_random_restarts
from simpleai.search import genetic
import random
from math import factorial


# FERHAT KÜRKÇÜOĞLU 200316040
# CENGİZHAN BAYRAM 200316066
# Pyhton 3.11

class NQueens(SearchProblem):
    def __init__(self, N, initial_state=None):
        self.N = N
        self.state = ""
        if initial_state is None:
            self.state = self._set_state()
            self.initial_state = self.state
        else:
            self.state = initial_state
            self.initial_state = initial_state

    def __str__(self):
        return f"{self.N}X{self.N} NQueens board is initialized with state {self.state}"

    def actions(self, state):
        possible_actions = []
        for queen_col in range(self.N):
            for row in range(self.N):
                if str(row + 1) != state[queen_col]:
                    possible_actions.append((queen_col, row + 1))
        return possible_actions

    def result(self, state, action):
        new_state = list(state)
        col, row = action
        new_state[col] = str(row)
        return ''.join(new_state)

    def is_goal(self, state):
        return self._count_attacking_pairs(state) == 0

    def heuristic(self, state):
        return self._count_attacking_pairs(state)

    def value(self, state):
        return (int(factorial(self.N)/(factorial(self.N - 2) * factorial(2)))) - self._count_attacking_pairs(state)

    def crossover(self, state1, state2):
        crossoverp = random.randint(1, self.N-1)
        new_state = state1[:crossoverp] + state2[crossoverp:]
        return new_state

    def mutate(self, state):
        if random.random() < 0.0001:
            rand_value = random.randint(0, self.N - 1)
            mutation_value = str(random.randint(1, self.N))

            new_value = state[:rand_value] + mutation_value + state[rand_value + 1:]
            return new_value
        else:
            return state


    def _set_state(self):
        print("Press 1 to enter the state manually.")
        print("Press 2 to generate a random state.")
        choice = input()
        if choice == "1":
            while True:
                entered_state = input("Please enter the state manually: ")
                if self._is_valid(entered_state):
                    return entered_state
                else:
                    print("Invalid state! Please try again.")
        else:
            return self.generate_random_state()

    def generate_random_state(self):
        for i in range(self.N):
            self.state += str(random.randint(1, self.N))
        return self.state

    def _is_valid(self, state):
        if len(state) != self.N or "0" in state or not state.isdigit() or any(
                char.isdigit() and int(char) > self.N for char in state):
            return False
        else:
            return True

    def _count_attacking_pairs(self, state):
        number_of_attacking_pairs = 0
        for i in range(self.N):
            for j in range(i + 1, self.N):
                if state[i] == state[j] or abs(i - j) == abs(int(state[i]) - int(state[j])):
                    number_of_attacking_pairs += 1
        return number_of_attacking_pairs


nqueens_problem = NQueens(4)
# genetic_algorithm = genetic(nqueens_problem, 100, 0.1, 1)
# hill_climbing_random_restarts = hill_climbing_random_restarts(nqueens_problem, 5)
breadth_first_search = breadth_first(nqueens_problem)
# depth_first_search = depth_first(nqueens_problem)
# uniform_search = uniform_cost(nqueens_problem)
# greedy_search = greedy(nqueens_problem)
# a_star = astar(nqueens_problem)
# iterative_search = iterative_limited_depth_first(nqueens_problem)
# limited_search = limited_depth_first(nqueens_problem)

print("Solution:", breadth_first_search.state)

