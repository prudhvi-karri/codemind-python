def preety(l):
    r=l%10
    if r==2 or r==3 or r==9:
        return 1
    return 0
n=int(input())
while n:
    a,b=map(int,input().split())
    c=0
    for i in range(a,b+1):
        if preety(i):
            #print(i,end=' ')
            c+=1
    print(c)
    n-=1