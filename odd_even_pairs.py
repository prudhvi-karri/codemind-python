v=int(input())
l=list(map(int,input().split()))
m,n,i=[],[],0
for i in l:
    if i%2:
        m.append(i)
    else:
        n.append(i)
i,j=0,0
#print(m,n)
while i+j<v:
    if len(m)!=0:
        print(m[0],end=' ')
        m.pop(0)
        i+=1
    if len(n)!=0:
        print(n[0],end=' ')
        n.pop(0)
        j+=1
if v%2:
    print(0)