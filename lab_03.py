class A_SEARCH:
    def __init__(self, state, parent=None, move=None, g_cost=0, h_cost=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.g_cost = g_cost 
        self.h_cost = h_cost 
        self.f_cost = g_cost + h_cost  


