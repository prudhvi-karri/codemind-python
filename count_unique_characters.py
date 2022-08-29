n=input().lower()
s=sorted(n)
n=set(n)
#print(s,n)
c=0
for i in n:
    if i!=' ':
        if s.count(i)==1:
            c+=1
print(c)