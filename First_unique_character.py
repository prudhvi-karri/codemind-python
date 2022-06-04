n=input()
k=0
for i in range(len(n)):
    c=0
    for j in range(len(n)):
        if i!=j and n[i]==n[j]:
            c+=1
    if c==0:
        print(n[i])
        k=1
        break
if k==0:
    print(-1)