n,m=map(int,input().split())
l=list(map(int,input().split()))
l1=list(map(int,input().split()))
k=[]
for i in l:
    if i in l1 and i not in k:
        k.append(i)
print(*k)