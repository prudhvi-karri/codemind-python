n=int(input())
while n:
    a=int(input())
    s,i=0,0
    while a:
        d=a%10
        s+=d*(2**i)
        i+=1
        a//=10
    print(s)
    n-=1