n=int(input())
while n:
    a=input()
    k,j,s,l=0,0,1,[]
    for i in range(len(a)-1,-1,-1):
        k+=(int(a[i])*(2**j))
        j+=1
        if s%3==0:
            l.append(str(k))
            k=0
            j=0
        s+=1
    l.append(str(k))
    l=''.join(l)
    l=l[::-1]
    print(int(l))
    n-=1