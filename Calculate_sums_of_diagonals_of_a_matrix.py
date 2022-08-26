n=int(input())
mat=[]
for i in range(n):
    v=[]
    v=list(map(int,input().split()))
    mat.append(v)
s=s1=0
for i in range(n):
    for j in range(n):
        if i==j:
            s+=mat[i][j]
k=n
for i in range(n):
    s1+=mat[i][k-1]
    k-=1
print("Principal Diagonal:"+str(s))
print("Secondary Diagonal:"+str(s1))