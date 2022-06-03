n=input().lower()
m=input().lower()
n="".join(n)
m="".join(m)
l=[]
c=0
for i in range(len(m)):
    i=m[i]
    if i in n and i not in l and i!=' ':
        c+=1
        l.append(i)
print(c)