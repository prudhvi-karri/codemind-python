n=input()
a=['a','e','i','o','u']
b=[]
for i in range(len(n)):
    if n[i] in a:
        b.append(n[i])
c=0
for i in range(len(a)):
    if a[i] not in b:
        print(a[i],end=' ')
    else:
        c+=1
if c==5:
    print(0)