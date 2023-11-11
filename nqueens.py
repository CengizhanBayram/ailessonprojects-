import random

class NQueens():
    """Class to represent the N-Queens problem."""

    def __init__(self, N):
        """Class constructor initializes the instance attributes N and state."""
        self.N = N
        self.state = None
        self._set_state()

    def __str__(self):
        """Returns a formatted string that represents the instance."""
        return f"N-Queens Board (N={self.N})\n{self.state}"

    def _set_state(self):
        """Sets the instance attribute state by displaying a menu to the user.
        The user either enters the state manually or prompts the system to generate a random state.
        Checks if the input state is a valid state."""
        choice = input("Do you want to enter the state manually? (y/n): ").lower()
        if choice == 'y':
            self.state = self._get_user_input_state()
        else:
            self.state = self.generate_random_state()

        while not self._is_valid(self.state):
            print("Invalid state. Please enter a valid state.")
            self.state = self._get_user_input_state()

    def _get_user_input_state(self):
        """Gets user input for the state."""
        state_str = input(f"Enter the state as a string of {self.N} numbers separated by spaces: ")
        return list(map(int, state_str.split()))

    def generate_random_state(self):
        """Generates and returns a valid random state."""
        return random.sample(range(1, self.N + 1), self.N)

    def _is_valid(self, state):
        """Checks if the input state is a valid state."""
        if len(set(state)) == len(state) == self.N:
            return all(1 <= queen <= self.N for queen in state)
        return False

    def _count_attacking_pairs(self, state):
        """Counts the number of attacking pairs in the given state board."""
        attacking_pairs = 0
        for i in range(self.N - 1):
            for j in range(i + 1, self.N):
                if state[i] == state[j] or abs(i - j) == abs(state[i] - state[j]):
                    attacking_pairs += 1
        return attacking_pairs

# Example usage:
N = 8  # Change this to the desired size of the board
n_queens_instance = NQueens(N)
print(n_queens_instance)
attacking_pairs = n_queens_instance._count_attacking_pairs(n_queens_instance.state)
print(f"Number of attacking pairs: {attacking_pairs}")
# This is a test code. You can try with different N values and states.
problem = NQueens(5) #create NQueens instance
print(problem) #print the description of the problem
print(problem._count_attacking_pairs(problem.state)) #print the total number of attacking pairs in the boardn
