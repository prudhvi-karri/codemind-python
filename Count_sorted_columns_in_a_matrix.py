n,m=map(int,input().split())
mat=[]
for i in range(n):
    v=[]
    v=list(map(int,input().split()))
    mat.append(v)
s=0
for i in range(m):
    k=[]
    for j in range(n):
        k.append(mat[j][i])
    if k==sorted(k) or k==sorted(k,reverse=True):
        s+=1
print(s)