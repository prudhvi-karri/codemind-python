n,m=map(int,input().split())
mat=[]
for i in range(n):
    v=[]
    v=list(map(int,input().split()))
    mat.append(v)
s=0
for k in mat:
    if k==sorted(k) or k==sorted(k,reverse=True):
        s+=1
print(s)