def happy(a, ex):
    if a==1:
        return "HAPPY"
    if a in ex:
        return "UNHAPPY"
    ex.append(a)
    temp=0
    temp+=(a%10)**2
    while int(a/10)!=0:
        a=int(a/10)
        temp+=(a%10)**2
    return happy(temp, ex)

n=int(input())
print(happy(n, []))
