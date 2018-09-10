def calc(a):
    temp = [0, 1, 2, 4]
    if a==0 :
        print(temp[0])
    elif a==1 :
        print(temp[1])
    elif a==2 :
        print(temp[2])
    elif a==3 :
        print(temp[3])
    else :
        for k in range(4, a+1):
            temp.append(temp[k-1]+temp[k-2]+temp[k-3])
        print(temp[a])

if __name__== "__main__":
    n = int(input())
    input_number = []
    for i in range(0, n):
        input_number.append(int(input()))
    for i in input_number:
        calc(i)
