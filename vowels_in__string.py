s=input()
k="aeiouAEIOU"
c=0
l=[]
for i in s:
    if i in k:
        if i not in l:
            c=1
            l.append(i)
print(*l)
if c==0:
    print("-1")