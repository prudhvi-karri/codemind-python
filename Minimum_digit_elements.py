n=int(input())
l=list(map(int,input().split()))
a=[]
for i in l:
    t=i
    c=0
    while t:
        d=t%10
        c+=1
        t//=10
    a.append(c)
p=min(a)
s=0
for i in a:
    if i==p:
        s+=1
print(s)