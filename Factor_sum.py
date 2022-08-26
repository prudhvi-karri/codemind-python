def sum_of_fact(m):
    s=0
    for i in range(1,m+1):
        if m%i==0:
            s+=i
    return s
l=input()
l=l.split(',')
o=[]
for i in l:
    o.append(int(i))
v=[]
for i in o:
    k=sum_of_fact(int(i))
    #print(k)
    if k in o:
        v.append(i)
if v==[]:
    print(-1)
else:
    print(*sorted(v))