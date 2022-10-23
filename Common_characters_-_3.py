b=input().lower().split()
k=b[0]
v=[]
for j in k:
    s=1
    for i in range(1,len(b)):
        if j in b[i]:
            s+=1
    if s==len(b):
        v.append(j)
if v==[]:
    print(-1)
else:
    v=sorted(v)
    print(v[0])