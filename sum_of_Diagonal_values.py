n,m=map(int,input().split())
mat=[]
for i in range(n):
    v=[]
    v=list(map(int,input().split()))
    mat.append(v)
s=s1=0
for i in range(n):
    for j in range(n):
        if i==j :
            if n%2 and i==n//2:
                s+=0
            else:
                s+=mat[i][j]
k=n
for i in range(n):
    s1+=mat[i][k-1]
    k-=1
print(s+s1)