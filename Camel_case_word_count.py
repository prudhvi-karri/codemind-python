n=input()
c=1
for i in range(1,len(n)):
    if n[i].isupper():
        c+=1
print(c)