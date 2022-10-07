n=int(input())
while n:
    a=input()
    k=''
    for i in range(len(a)):
        h=int(a[i])
        s=''
        while h:
            d=h%2
            s+=str(d)
            h//=2
        if len(s)==0:
            s+='000'
        elif len(s)==2:
            s+='0'
        elif len(s)==1:
            s+='00'
        k+=s[::-1]
    print(int(k))
    n-=1