class AlphaBetaPruning:
    def __init__(self, depth, game_state, player):
        self.depth = depth
        self.game_state = game_state
        self.player = player
        self.node_count = 0
   
    def is_terminal(self, state):
        for i in range(3):
            if state[i][0] == state[i][1] == state[i][2] and state[i][0] != ' ':
                return True
            if state[0][i] == state[1][i] == state[2][i] and state[0][i] != ' ':
                return True
        if state[0][0] == state[1][1] == state[2][2] and state[0][0] != ' ':
            return True
        if state[0][2] == state[1][1] == state[2][0] and state[0][2] != ' ':
            return True
        for j in range (3):
            if state[i][j] == ' ':
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

    def alphabeta(self, state, depth, alpha, beta, maximizing_player):
        self.node_count += 1
        if depth == 0 or self.is_terminal(state):
            return self.utility(state)

        if maximizing_player:
            max_eval = float('-inf')
            for i in range(3):  
                    for j in range(3):  
                        if state[i][j] == ' ':  
                            state[i][j] = 'X'  
                            eval = self.alphabeta(state, depth - 1, alpha, beta, False)
                            state[i][j] = ' '  
                            max_eval = max(max_eval, eval)
                            alpha = max(alpha, eval)
                            if beta <= alpha:
                                break
            return max_eval
        else:
            min_eval = float('inf')
            for i in range(3):
                for j in range(3):  
                    if state[i][j] == ' ': 
                        state[i][j] = 'O'  
                        eval = self.alphabeta(state, depth - 1, alpha, beta, True)
                        state[i][j] = ' '  
                        min_eval = min(min_eval, eval)
                        beta = min(beta, eval)
                        if beta <= alpha:
                            break

            return min_eval
    def best_move(self, state):
        self.node_count=0
        best_value = float('-inf')
        best_move = None
        
        for i in range(3):
            for j in range(3):
                if state[i][j] == ' ':
                    state[i][j] = 'X' 
                    score = self.alphabeta(state, self.depth - 1, float('-inf'), float('inf'), False)                 
                    state[i][j] = ' ' 
                    if score > best_value:
                        best_value = score
                        best_move = (i, j)
        print("Nodes evaluated by Alpha-Beta Pruning:", self.node_count)            
        return best_move

if __name__ == "__main__":
    initial_board = [
        ['X', ' ', 'X'],
        [' ', 'O', 'O '],
        [' ', ' ', ' ']
    ]

    difficulty_level = 5  
    alpha_beta_instance = AlphaBetaPruning(difficulty_level, initial_board, 'X')
    best_move = alpha_beta_instance.best_move(initial_board)
    print(f"The best move for X is: {best_move}")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

# def print_board(state):
#         """ Helper function to print the Tic-Tac-Toe board """
#         for row in state:
#             print("|".join(row))
#             print("-" * 5)


# def play_game():
#     print("Welcome to Tic-Tac-Toe!")
#     difficulty = int(input("Select difficulty level (1 to 5): "))
#     game_state = [[' ' for _ in range(3)] for _ in range(3)]
#     ai = AlphaBetaPruning(difficulty, game_state, 'X')

#     while True:
#         print_game_state(game_state)

#         while True:
#             row = int(input("Enter your move row (0, 1, or 2): "))
#             col = int(input("Enter your move column (0, 1, or 2): "))
#             if game_state[row][col] == ' ':
#                 game_state[row][col] = 'O'  
#                 break
#             else:
#                 print("Cell is already occupied. Try again.")

#         if ai.is_terminal(game_state):
#             print_game_state(game_state)
#             print("Game Over! You Win!" if ai.utility(game_state) == -1 else "Game Over! It's a Draw!" if ai.utility(game_state) == 0 else "Game Over! AI Wins!")
#             break
        
#         ai_move = ai.best_move(game_state)
#         game_state[ai_move[0]][ai_move[1]] = 'X'  

#         if ai.is_terminal(game_state):
#             print_game_state(game_state)
#             print("Game Over! You Win!" if ai.utility(game_state) == -1 else "Game Over! It's a Draw!" if ai.utility(game_state) == 0 else "Game Over! AI Wins!")
#             break


# def print_game_state(state):
#     for row in state:
#         print('|'.join(row))
#         print('-' * 5)

# play_game()
