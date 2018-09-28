def changeXY(is_x, is_y, number, pm) :
    if is_x==1:
        is_x=0
        is_y=1
        if number==1:
            pm*=-1
    elif is_y:
        is_x=1
        is_y=0
        if number==0:
            pm*=-1
    return is_x, is_y, pm

def moveXY(x, y, number, is_x, is_y, pm):
    x = x+pm*is_x*number
    y = y+pm*is_y*number
    return(x,y)

def answer(M, command, number,n):
    max=M
    x=0
    y=0
    is_x = 1
    is_y = 0
    pm = 1

    for i in range(0, n):
        if command[i]=='TURN':
            is_x, is_y, pm = changeXY(is_x, is_y, number[i], pm)
        if command[i]=='MOVE':
            x, y = moveXY(x, y,number[i], is_x, is_y, pm)
        if x < 0 or y < 0 or x > M or y > M :
            print(-1)
            break
        if i==n-1:
            print(x,y)

M, n = input().split()
command = []
number = []

for i in range(0, int(n)):
    com_num=input().split()
    command.append(com_num[0])
    number.append(int(com_num[1]))

answer(int(M), command, number, int(n))
