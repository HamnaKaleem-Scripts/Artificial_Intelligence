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

def is_goal(state):
    return state == goal_state


def iddfs(initial_state, max_depth=20):
    total_nodes_explored = 0
    total_moves = 0
    
    for depth in range(max_depth + 1):
        print(f"IDDFS: Searching with depth limit {depth}")
        found, nodes, moves, path = dfs(initial_state, depth)
        total_nodes_explored += nodes
        total_moves += moves
        if found:
            print("IDDFS: Goal reached!")
            print(f"Total number of moves: {total_moves}")
            print(f"Total nodes explored: {total_nodes_explored}")
            print("Path to goal:")
            for step in path: 
                for row in step:
                    print(row)
                print()  
            return True
    print("IDDFS: Goal not reachable ")
    return False


def dfs(initial_state, depth_limit):
    stack = []
    stack.append((initial_state, 0, [])) 
    
    visited = set()
    visited.add(state_to_string(initial_state))
    
    moves_count = 0
    nodes_explored = 0
    
    while stack:
        current_state, depth, path = stack.pop()
        nodes_explored += 1
        moves_count += 1
        

        current_path = path + [current_state]  
        
        if is_goal(current_state):
            return True, nodes_explored, moves_count, current_path  
        
        if depth < depth_limit:
            x, y = find_zero(current_state)
            for state in my_moves(current_state, x, y):
                state_str = state_to_string(state)
                if state_str not in visited:
                    visited.add(state_str)
                    stack.append((state, depth + 1, current_path)) 
    
    return False, nodes_explored, moves_count, []


def main():
    initial_state = [
        [1, 2, 3],
        [4, 0, 6],
        [7, 5, 8]
    ]
    
    print("Initial State:")
    for row in initial_state:
        print(row)

    print("\nSolving with IDDFS:")
    iddfs(initial_state, max_depth=20)

main()
