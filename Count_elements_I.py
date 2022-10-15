n,m=map(int,input().split())
l=list(map(int,input().split()))
l1=list(map(int,input().split()))
c=0
l=set(l)
for i in l:
    if i in l1:
        c+=1
print(c)