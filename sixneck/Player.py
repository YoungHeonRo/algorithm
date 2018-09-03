class Player():
    
    def __init__(self, color):
        self.color = color
        
    def get_move(self, board):
        try:
            move = input('enter your move (x, y): ')
            x, y = move.split(",")
            x = int(x)
            y = int(y)
        except Exception as e:
            x = -1
        if x < 0 or y < 0 or x >= board.col or y >= board.row or board.state[y][x] != 0:
            print('invalid move')
            return self.get_move(board)
        return x, y

class rule_based_AI():

    def __init__(self, color):
        self.color = color

    def get_move(self, board):
        b_priority = []
        w_priority = []
        for i, row in enumerate(board.state):
            for j, value in enumerate(row):
                if value == 0:
                    b_priority.append([i, j, board.b_priority[i][j]])
                    w_priority.append([i, j, board.w_priority[i][j]])
        
        b_priority.sort(key = self.my_sort)
        w_priority.sort(key = self.my_sort)
        
        if self.color == 1:
            my = b_priority
            enemy = w_priority
        else:
            my = b_priority
            enemy = w_priority

        if my[-1][-1] >= enemy[-1][-1]:
            y = my[-1][0]
            x = my[-1][1]
        else:
            y = enemy[-1][0]
            x = enemy[-1][1]

        return x, y

        
            

    def my_sort(self, x):
        return x[-1]
            

        
def init_player(color, option):
    if option == 'rb':
        return rule_based_AI(color)
    return Player(color)
