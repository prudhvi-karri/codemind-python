a=input().lower()
b=input().lower()
a=sorted(a)
b=sorted(b)
c=sorted(set(a))
d=sorted(set(b))
s=[]
for i in c:
    if i not in b and i!=' ':
            s.append(i)
for i in d:
    if i not in a and i!=' ':
            s.append(i)
s=sorted(s)
s="".join(s)
print(s)