n=list(map(str,input().lower().split()))
m=list(map(str,input().lower().split()))
c=0
for i in n:
    if i in m:
        c+=1
print(c)