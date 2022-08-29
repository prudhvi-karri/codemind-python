a=input().lower()
b=input().lower()
a=sorted(a)
b=sorted(b)
c=sorted(set(a))
d=sorted(set(b))
s=0
for i in c:
    if i not in b and i!=' ':
            s+=1
for i in d:
    if i not in a and i!=' ':
            s+=1
print(s)