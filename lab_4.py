import heapq
class PuzzleNode:
    def __init__(self, state, parent, move, g_cost, h_cost):
        self.state=state
        self.parent = parent
        self.move = move
        self.g_cost = g_cost
        self.h_cost = h_cost
        self.f_cost=g_cost+h_cost
    def generate_children(self, goal_state):
        children=[]
        empty_index=self.state.index(0)
        possible_moves,=self.state.possible_state()
        for i in possible_moves:
            new_state=self.state.copy()
            new_state[empty_index],new_state[i]=new_state[i],new_state[empty_index]
            h_cost=PuzzleNode.calculate_heuristic(new_state,goal_state)
            child=PuzzleNode(new_state,self,i,self.g_cost+1,h_cost)
            children.append(child) 
    def possible_moves(self,empty_index):
        move_dict = {
        0: [1, 3],       
        1: [0, 2, 4],    
        2: [1, 5],       
        3: [0, 4, 6],     
        4: [1, 3, 5, 7],
        5: [2, 4, 8],     
        6: [3, 7],        
        7: [4, 6, 8],     
        8: [5, 7]         
        }
        return move_dict[empty_index]
    def calculate_heuristic(state,goal_state):
        distance = 0
        for i in range(len(state)):
            tile = state[i]
            if tile != 0:  
                current_row = i // 3
                current_col = i % 3
                target_index = goal_state.index(tile)
                target_row = target_index // 3
                target_col = target_index % 3
                distance += abs(current_row - target_row) + abs(current_col - target_col)
        return distance
class AStarSolver:
    def __init__(self, start_state, goal_state):
        self.start_state = start_state
        self.goal_state = goal_state
    def solve(self):
        open_list = []
        closed_set = set()
        start_node = PuzzleNode(self.start_state, None, None, 0, PuzzleNode.calculate_heuristic(self.start_state, self.goal_state, self.heuristic))
        heapq.heappush(open_list, (start_node.f_cost, start_node))

        while open_list:
            _, current_node = heapq.heappop(open_list)

            if current_node.state == self.goal_state:
                return self.trace_solution(current_node)

            closed_set.add(tuple(current_node.state))

            for child in current_node.generate_children(self.goal_state):
                if tuple(child.state) in closed_set:
                    continue
                heapq.heappush(open_list, (child.f_cost, child))
        return None
    def trace_solution(self, node):
        path = []
        current = node
        while current:
            path.append(current.state)
            current = current.parent
        return path[::-1]
        
    def is_solvable(state):
        inversions = 0
        n = len(state)
        for i in range(n):
            if state[i] != 0:
                for j in range(i + 1, n):
                    if state[j] != 0:
                        if state[i] > state[j]:
                            inversions += 1

        return inversions % 2 == 0
start_state = [1, 2, 3, 4, 0, 5, 6, 7, 8]  # Initial puzzle configuration
goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]    # Goal configuration

solver = AStarSolver(start_state, goal_state)
solution_path = solver.solve()

if solution_path:
    print("Solution found!")
    for step in solution_path:
        print(step)
else:
    print("No solution exists for the given start state.")