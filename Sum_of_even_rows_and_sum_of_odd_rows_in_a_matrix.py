n,m=map(int,input().split())
od,se=0,0
for i in range(n):
    l=[]
    l=list(map(int,input().split()))
    if i%2:
        od+=sum(l)
    else:
        se+=sum(l)
print(se,od)