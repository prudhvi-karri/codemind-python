n=int(input())
l=list(map(int,input().split()))
i=0
while i<n:
    for j in range(l[i+1]):
        print(l[i],end=' ')
    i+=2