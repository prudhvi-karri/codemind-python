n=input().lower().split()
k=n[0]
s=0
for i in k:
    c=0
    for j in n:
        if i in j:
            c+=1
    if c==len(n):
        s=1
        print(i,end='')
if s!=1:
    print(-1)