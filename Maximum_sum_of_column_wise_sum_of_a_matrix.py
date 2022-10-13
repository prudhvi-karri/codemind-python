n,m=map(int,input().split())
mat=[]
for i in range(n):
    v=[]
    v=list(map(int,input().split()))
    mat.append(v)
l=[]
for i in range(m):
    s=0
    for j in range(n):
        s+=mat[j][i]
    l.append(s)
print(max(l))