r,c=map(int,input().split())
mat=[]
for i in range(r):
    v=[]
    v=list(map(int,input().split()))
    mat.append(v)
s=0
for i in range(r):
    for j in range(c):
        if i==0 or j==0 or i==r-1 or j==c-1:
            s+=mat[i][j]
print(s)