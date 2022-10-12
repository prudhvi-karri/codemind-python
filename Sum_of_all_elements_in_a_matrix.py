n,m=map(int,input().split())
se=0
for i in range(n):
    l=[]
    l=list(map(int,input().split()))
    se+=sum(l)
print(se)