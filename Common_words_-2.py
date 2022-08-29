a=input().split()
b=input().split()
c=0
for i in a:
    if a.count(i)==1 and b.count(i)==1:
        if i in b:
            c+=1
print(c)