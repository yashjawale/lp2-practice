import heapq

# Define the goal state for the 8-puzzle problem
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

# Define a class to represent the puzzle state
class PuzzleState:
    def __init__(self, board, parent=None, move=""):
        self.board = board
        self.parent = parent
        self.move = move
        self.cost = 0
        self.depth = 0

        if parent:
            self.depth = parent.depth + 1

    # Define methods to compare puzzle states
    def __lt__(self, other):
        return self.cost < other.cost

    def __eq__(self, other):
        return self.board == other.board

# Define the heuristic function (number of tiles not in their correct place)
def misplaced_tiles(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state.board[i][j] != goal_state[i][j]:
                count += 1
    return count

# Define the A* search algorithm
def astar_search(initial_state):
    # Initialize the open list (priority queue) with the initial state
    open_list = []
    heapq.heappush(open_list, initial_state)

    # Initialize an empty set to store visited states
    visited = set()

    # Run the A* search algorithm
    while open_list:
        # Pop the state with the lowest cost from the open list
        current_state = heapq.heappop(open_list)

        # Check if the current state is the goal state
        if current_state.board == goal_state:
            # If yes, return the solution path
            path = []
            while current_state:
                path.append(current_state)
                current_state = current_state.parent
            return path[::-1]

        # Add the current state to the visited set
        visited.add(tuple(map(tuple, current_state.board)))

        # Generate all possible next states (moves) from the current state
        for move in ["up", "down", "left", "right"]:
            next_state = generate_next_state(current_state, move)

            # Check if the next state is valid and not already visited
            if next_state and tuple(map(tuple, next_state.board)) not in visited:
                # Calculate the cost of the next state
                next_state.cost = next_state.depth + misplaced_tiles(next_state)

                # Push the next state into the open list
                heapq.heappush(open_list, next_state)

    # If no solution is found, return None
    return None

# Define a function to generate the next state based on the current state and move
def generate_next_state(current_state, move):
    blank_row, blank_col = find_blank(current_state)

    if move == "up" and blank_row > 0:
        new_board = [row[:] for row in current_state.board]
        new_board[blank_row][blank_col], new_board[blank_row - 1][blank_col] = \
            new_board[blank_row - 1][blank_col], new_board[blank_row][blank_col]
        return PuzzleState(new_board, parent=current_state, move="Up")

    elif move == "down" and blank_row < 2:
        new_board = [row[:] for row in current_state.board]
        new_board[blank_row][blank_col], new_board[blank_row + 1][blank_col] = \
            new_board[blank_row + 1][blank_col], new_board[blank_row][blank_col]
        return PuzzleState(new_board, parent=current_state, move="Down")

    elif move == "left" and blank_col > 0:
        new_board = [row[:] for row in current_state.board]
        new_board[blank_row][blank_col], new_board[blank_row][blank_col - 1] = \
            new_board[blank_row][blank_col - 1], new_board[blank_row][blank_col]
        return PuzzleState(new_board, parent=current_state, move="Left")

    elif move == "right" and blank_col < 2:
        new_board = [row[:] for row in current_state.board]
        new_board[blank_row][blank_col], new_board[blank_row][blank_col + 1] = \
            new_board[blank_row][blank_col + 1], new_board[blank_row][blank_col]
        return PuzzleState(new_board, parent=current_state, move="Right")

    else:
        return None

# Define a function to find the position of the blank tile
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state.board[i][j] == 0:
                return i, j

# Define a function to print the solution path
def print_solution(path):
    for i, state in enumerate(path):
        print(f"Step {i}: {state.move}")
        print_board(state.board)
        print()

# Define a function to print the puzzle board
def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))

# Main function
def main():
    # Define the initial state of the puzzle
    initial_state = PuzzleState([[1, 2, 3], [4, 0, 5], [7, 8, 6]])

    # Run the A* search algorithm to solve the puzzle
    solution_path = astar_search(initial_state)

    # Print the solution path
    if solution_path:
        print("Solution found!")
        print_solution(solution_path)
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
