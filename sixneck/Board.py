class Board:
    
    # need documentation
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.state = [[0 for i in range(col)] for j in range(row)]
        self.count = 0
        self.b_priority = [[0 for i in range(col)] for j in range(row)]
        self.b_max = [[[0 for i in range(col)] for j in range(row)] for k in range(4)]
        self.b_dup = [[[0 for i in range(col)] for j in range(row)] for k in range(4)]
        self.w_priority = [[0 for i in range(col)] for j in range(row)]
        self.w_max = [[[0 for i in range(col)] for j in range(row)] for k in range(4)]
        self.w_dup = [[[0 for i in range(col)] for j in range(row)] for k in range(4)]

    def print(self):
        symbol = ['.', 'o', 'x']

        line = '\n '
        for i in range(self.col):
            line = line + format(i, '3d') + ' '
        print(line + ' x')
        
        for i in range(self.row):
            line = format(i, '2d') + ' '
            for j in range(self.col):
                line += symbol[self.state[i][j]] + '   '
            print(line + '\n')
        print('y\n')
    
    # update the move and print the board
    # (input: x, y of the move and player's color / output: is_end, winner)
    def update(self, x, y, color):
        self.state[y][x] = color
        self.count += 1
        self.print()
        return self.check(x, y)
    
    # check if the game is end (input: x, y of the last move / output: is_end, winner)
    def check(self, x, y):
        x_max = x + 5 if x + 5 < self.col else self.col - 1
        x_min = x - 5 if x - 5 >= 0 else 0
        y_max = y + 5 if y + 5 < self.row else self.row - 1
        y_min = y - 5 if y - 5 >= 0 else 0

        for i in range(y_min, y_max - 5 + 1):
            if len(set(self.state[j][x] for j in range(i, i + 6))) == 1:
                return True, self.state[y][x]

        for i in range(x_min, x_max - 5 + 1):
            if len(set(self.state[y][j] for j in range(i, i + 6))) == 1:
                return True, self.state[y][x]

        minus = -min(x - x_min, y - y_min)
        plus = min(x_max - x, y_max - y) - 5
        for i in range(minus, plus + 1):
            if len(set(self.state[y + j][x + j] for j in range(i, i + 6))) == 1:
                return True, self.state[y][x]

        minus = -min(x - x_min, y_max - y)
        plus = min(x_max - x, y - y_min) - 5
        for i in range(minus, plus + 1):
            if len(set(self.state[y - j][x + j] for j in range(i, i + 6))) == 1:
                return True, self.state[y][x]
            
        if self.count >= self.row * self.col:
            return True, -1

        return False, -1

    # update for rule based AI
    def update_rb(self, x, y, color):
        self.state[y][x] = color
        self.count += 1
        self.print()
        return self.check_rb(x, y)

    # special check algorithm for rule based AI
    def check_rb(self, x, y):
        x_max = x + 5 if x + 5 < self.col else self.col - 1
        x_min = x - 5 if x - 5 >= 0 else 0
        y_max = y + 5 if y + 5 < self.row else self.row - 1
        y_min = y - 5 if y - 5 >= 0 else 0

        for i in range(y_min, y_max - 5 + 1):
            box = list((j, x) for j in range(i, i + 6))
            box_state = list(self.state[y][x] for y, x in box)
            if len(set(box_state)) == 1:
                return True, self.state[y][x]
            self.update_priority(0, box, box_state)

        for i in range(x_min, x_max - 5 + 1):
            box = list((y, j) for j in range(i, i + 6))
            box_state = list(self.state[y][x] for y, x in box)
            if len(set(box_state)) == 1:
                return True, self.state[y][x]
            self.update_priority(1, box, box_state)

        minus = -min(x - x_min, y - y_min)
        plus = min(x_max - x, y_max - y) - 5
        for i in range(minus, plus + 1):
            box = list((y + j, x + j) for j in range(i, i + 6))
            box_state = list(self.state[y][x] for y, x in box)
            if len(set(box_state)) == 1:
                return True, self.state[y][x]
            self.update_priority(2, box, box_state)

        minus = -min(x - x_min, y_max - y)
        plus = min(x_max - x, y - y_min) - 5
        for i in range(minus, plus + 1):
            box = list((y - j, x + j) for j in range(i, i + 6))
            box_state = list(self.state[y][x] for y, x in box)
            if len(set(box_state)) == 1:
                return True, self.state[y][x]
            self.update_priority(3, box, box_state)

        if self.count >= self.row * self.col:
            return True, -1

        return False, -1

    def update_priority(self, direction, box, box_state):
        black_count = box_state.count(1)
        white_count = box_state.count(2)
        if black_count > 0 and white_count > 0:
            for y, x in box:
                self.b_priority[y][x] = -1
                self.w_priority[y][x] = -1
        if black_count > 0:
            for y, x in box:
                if black_count > self.b_max[direction][y][x]:
                    self.b_max[direction][y][x] = black_count
                    self.b_dup[direction][y][x] = 1
                    #수정 요망
                    self.b_priority[y][x] = max(list(self.b_max[i][y][x] for i in range(4)))
                elif black_count == self.b_max[direction][y][x]:
                    self.b_dup[direction][y][x] += 1
        else:
            for y, x in box:
                if white_count > self.w_max[direction][y][x]:
                    self.w_max[direction][y][x] = white_count
                    self.w_dup[direction][y][x] = 1
                    #수정 요망
                    self.w_priority[y][x] = max(list(self.w_max[i][y][x] for i in range(4)))
                elif white_count == self.w_max[direction][y][x]:
                    self.w_dup[direction][y][x] += 1


