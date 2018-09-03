from Player import *
from Board import *

#고정값
black = 1
white = 2
row = 15
col = 15

#임의로 설정하는 값
player1 = init_player(black, 'human')
player2 = init_player(white, 'rb')

#게임 시작
try:
    board = Board(row, col)
    board.update_rb(7, 7, black) #흑팀의 첫수는 정중앙에 놓는다. 
    while True:
        #누구의 턴인가?
        if board.count % 4 == 0 or board.count % 4 == 3:
            player = player1
        else:
            player = player2
        #first move
        x, y = first_move = player.get_move(board)
        is_end, winner = board.update_rb(x, y, player.color)
        if is_end:
            if winner == -1:
                print('draw')
            else:
                print('winner is player', winner)
            break
        #second move
        x, y = second_move = player.get_move(board)
        is_end, winner = board.update_rb(x, y, player.color)
        if is_end:
            if winner == -1:
                print('draw')
            else:
                print('winner is player', winner)
            break
        
except KeyboardInterrupt:
    print('\nbye')




