class Minimax:
    def __init__(self, game_state):
        self.game_state = game_state 
        self.node_count = 0 
    def is_terminal(self, state):
        for row in range(3):
            if state[row][0] == state[row][1] == state[row][1] != ' ':
                return True
        for col in range(3):
            if state[0][col] == state[1][col] == state[2][col] != ' ':
                return True
        if state[0][0] == state[1][1] == state[2][2] != ' ':
            return True
        if state[0][2] == state[1][1] == state[2][0] != ' ':
            return True
        for row in state:
            for cell in row:
                if cell == ' ':
                    return False 
        return True  

    def utility(self, state):
        for i in range(3):
            if state[i][0] == state[i][1] == state[i][1] != ' ': 
                if state[i][0]=='x':
                    return 1
                else :
                    return -1
        for j in range(3):
            if state[0][j] == state[1][j] == state[2][j] != ' ': 
                if state[j][0]=='x':
                    return 1
                else :
                    return -1
        if state[0][0] == state[1][1] == state[2][2] != ' ':  
            if state[0][0]=='x':
                    return 1
            else :
                    return -1
        if state[0][2] == state[1][1] == state[2][0] != ' ':  
            if state[0][0]=='x':
                    return 1
            else :
                    return -1
        return 0  

    def minimax(self, state, depth, maximizing_player):
        self.node_count += 1
        if self.is_terminal(state):
            return self.utility(state)
        if maximizing_player:  
            max_eval = float('-inf')
            for i in range(3):
                for j in range(3):
                    if state[i][j] == ' ':  
                        state[i][j] = 'X'  
                        current_score = self.minimax(state, depth + 1, False)
                        state[i][j] = ' '  
                        max_eval = max(max_eval, current_score)
            return max_eval
        else:  
            min_eval = float('inf')
            for i in range(3):
                for j in range(3):
                    if state[i][j] == ' ':
                        state[i][j] = 'O'  
                        current_score = self.minimax(state, depth + 1, True)
                        state[i][j] = ' '  
                        min_eval = min(min_eval, current_score)
            return min_eval

    def best_move(self, state):
        self.node_count = 0
        best_eval = float('-inf')
        move = None
        for i in range(3):
            for j in range(3):
                if state[i][j] == ' ': 
                    state[i][j] = 'X'  
                    current_score = self.minimax(state, 0, False)
                    state[i][j] = ' '  
                    if current_score > best_eval:
                        best_eval = current_score
                        move = (i, j) 
        print(f"Nodes evaluated by Minimax: {self.node_count}") 
        return move  

if __name__ == "__main__":
    initial_board = [
        ['x ', ' ', ' '],
        [' ', ' o', ' '],
        [' ', ' ', ' ']
    ]

    minimax = Minimax(initial_board)
    best_move = minimax.best_move(initial_board)
    print(f"The best move for X is: {best_move}")
