n=int(input())
while n:
    a=int(input())
    s=''
    while a:
        d=a%2
        s+=str(d)
        a//=2
    print(s[::-1])
    n-=1