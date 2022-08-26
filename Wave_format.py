n=int(input())
l=list(map(int,input().split()))
l=sorted(l)
l.reverse()
for i in range(0,n-1,2):
    t=l[i]
    l[i]=l[i+1]
    l[i+1]=t
print(*l)    