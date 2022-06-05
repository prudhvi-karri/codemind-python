n=int(input())
l=list(map(int,input().split()))
s=k=0
for i in range(n-1,-1,-1):
    s+=(l[i]*(2**k))
    k+=1
print(s)