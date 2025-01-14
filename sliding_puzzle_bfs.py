goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def my_moves(state, x, y):
    moves = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
    }
    
    pos_states = []

    for i in moves:
        dx, dy = moves[i]
        new_x = x + dx
        new_y = y + dy

        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            pos_states.append(new_state)
    return pos_states

def state_to_string(state):
    result = ""
    for row in state:
        for num in row:
            result += str(num)
    return result

def bfs(initial_state):
    queue = []
    queue.append(initial_state)
    
    visited = set()
    visited.add(state_to_string(initial_state))
    
    moves_count = 0
    nodes_explored = 0
    
    while queue:
        current_state = queue.pop(0)
        nodes_explored += 1
        moves_count += 1
        
        if current_state == goal_state:
            print("BFS: Goal reached!")
            print(f"Number of moves: {moves_count}")
            print(f"Nodes explored: {nodes_explored}")
            return True
        
        x, y = find_zero(current_state)
        for state in my_moves(current_state, x, y):
            state_str = state_to_string(state)
            if state_str not in visited:
                visited.add(state_str)
                queue.append(state)
    
    print("BFS: Goal not reachable.")
    return False

def main():
    initial_state = [
        [1, 2, 3],
        [4, 0, 6],
        [7, 5, 8]
    ]
    
    print("Initial State:")
    for row in initial_state:
        print(row)
    print("\nSolving with BFS:")
    bfs(initial_state)

main()
