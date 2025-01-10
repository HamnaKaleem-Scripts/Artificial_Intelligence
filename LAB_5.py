import heapq
class Node:
    def __init__(self, state, parent, move, h_cost):
        self.state = state           
        self.parent = parent         
        self.move = move              
        self.h_cost = h_cost          
    def __lt__(self, other):
        return self.h_cost < other.h_cost
    def possible_moves(self, empty_index):
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

    def generate_children(self):
        children = []
        empty_index = self.state.index(0)
        possible_moves = self.possible_moves(empty_index) 
        for i in possible_moves:
            new_state = self.state.copy()
            new_state[empty_index], new_state[i] = new_state[i], new_state[empty_index]
            child = Node(new_state, self, i, 0)
            children.append(child)
        return children  

    def calculate_heuristic(self, goal_state):
        distance = 0
        for i in range(len(self.state)):
            tile = self.state[i]
            if tile != 0:  
                current_row = i // 3
                current_col = i % 3
                target_index = goal_state.index(tile)
                target_row = target_index // 3
                target_col = target_index % 3
                distance += abs(current_row - target_row) + abs(current_col - target_col)
        return distance


class GreedyBestFirstSearch:
    def __init__(self, start_state, goal_state):
        self.start_state = start_state
        self.goal_state = goal_state
        self.open_list = []  
        self.explored = set()  

    def solve(self):
        start_node = Node(self.start_state, None, None, 0)
        start_node.h_cost = start_node.calculate_heuristic(self.goal_state)

        heapq.heappush(self.open_list, (start_node.h_cost, start_node))

        while self.open_list:

            a, current_node = heapq.heappop(self.open_list)
            if current_node.state == self.goal_state:
                return self.trace_solution(current_node)
            self.explored.add(tuple(current_node.state))
            for child in current_node.generate_children():
                child.h_cost = child.calculate_heuristic(self.goal_state)
                if tuple(child.state) not in self.explored:
                    self.explored.add(tuple(child.state))
                    heapq.heappush(self.open_list, (child.h_cost, child))

        return None  
    def trace_solution(self, node):
        path = []
        current = node
        while current:
            path.append(current.state)
            current = current.parent
        return path[::-1]

def main():
    start_state = [1, 2, 3,
                   4, 0, 5,
                   6, 7, 8]  
    goal_state = [1, 2, 3,
                  4, 5, 6,
                  7, 8, 0]
    solver = GreedyBestFirstSearch(start_state, goal_state)
    solution = solver.solve()
    if solution:
        print("Solution found! Moves to solve the puzzle:")
        for move in solution:
            print(move)
    else:
        print("No solution found.")
main()
