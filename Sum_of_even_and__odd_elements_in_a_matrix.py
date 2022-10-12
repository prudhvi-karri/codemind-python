n,m=map(int,input().split())
od,se=0,0
for i in range(n):
    l=[]
    l=list(map(int,input().split()))
    for j in l:
        if j%2:
            od+=j
        else:
            se+=j
print(se,od)