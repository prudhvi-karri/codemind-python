n,m=map(int,input().split())
max=0
for i in range(n):
    v=[]
    v=list(map(int,input().split()))
    if sum(v)>max:
        max=sum(v)
print(max)