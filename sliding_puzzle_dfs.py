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
    
    poss_states = []

    for i in moves:
        dx, dy = moves[i]
        new_x = x + dx
        new_y = y + dy

        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            poss_states.append(new_state)
    return poss_states

def state_to_string(state):
    result = ""
    for row in state:
        for num in row:
            result += str(num)
    return result

def dfs(initial_state, depth_limit=20):
    stack = []
    stack.append((initial_state, 0))
    
    visited = []
    visited.append(state_to_string(initial_state))
    
    moves_count = 0
    nodes_explored = 0
    
    while stack:
        current_state, depth = stack.pop()
        nodes_explored += 1
        moves_count += 1
        
        if current_state==goal_state:
            print("DFS: Goal reached!")
            print(f"Number of moves: {moves_count}")
            print(f"Nodes explored: {nodes_explored}")
            return True
        
        if depth < depth_limit:
            x, y = find_zero(current_state)
            
            for state in my_moves(current_state, x, y):
                state_str = state_to_string(state)
                if state_str not in visited:
                    visited.append(state_str)
                    stack.append((state, depth + 1))
    
    print("DFS: Goal not reachable within depth limit.")
    return False

def main():
    initial_state = [
        [1, 2, 3],
        [4, 0, 6],
        [7, 5, 8]
    ]   
    print("Initial State:")
    for i in initial_state:
        print(i)
    print("\nSolving with DFS:")
    dfs(initial_state, depth_limit=20)
main()
