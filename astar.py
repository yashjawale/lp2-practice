# Define the goal state
goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]

# Define the heuristic function (Manhattan distance)
def heuristic(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                x_goal, y_goal = divmod(state[i][j] - 1, 3)
                distance += abs(i - x_goal) + abs(j - y_goal)
    return distance

# Define a function to find the possible moves
def possible_moves(state):
    moves = []
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                if i > 0:
                    moves.append((i - 1, j))
                if i < 2:
                    moves.append((i + 1, j))
                if j > 0:
                    moves.append((i, j - 1))
                if j < 2:
                    moves.append((i, j + 1))
                return moves

# Define a function to generate successor states
def successors(state, move):
    new_state = [row[:] for row in state]
    i, j = move
    zero_i, zero_j = [(x, y) for x in range(3) for y in range(3) if state[x][y] == 0][0]
    new_state[zero_i][zero_j], new_state[i][j] = new_state[i][j], new_state[zero_i][zero_j]
    return new_state

# Define the A* algorithm
def astar(start_state):
    visited = set()
    queue = [(0, start_state)]
    queue.sort(key=lambda x: x[0] + heuristic(x[1]))
    
    while queue:
        cost, state = queue.pop(0)
        
        if state == goal_state:
            return state
        
        visited.add(tuple(map(tuple, state)))
        
        for move in possible_moves(state):
            next_state = successors(state, move)
            if tuple(map(tuple, next_state)) not in visited:
                queue.append((cost + 1, next_state))
                queue.sort(key=lambda x: x[0] + heuristic(x[1]))
    
    return None

# Define a function to print the path from start to goal state
def print_path(path):
    for state in path:
        for row in state:
            print(row)
        print()

# Example usage
start_state = [[1, 2, 3],
               [4, 0, 6],
               [7, 5, 8]]

path = astar(start_state)
if path:
    print("Solution found:")
    print_path(path)
else:
    print("No solution found.")
