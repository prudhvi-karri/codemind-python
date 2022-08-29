n=input().lower()
s=sorted(n)
n=sorted(set(n))
c=0
for i in n:
    if i!=' ':
        if s.count(i)==1:
            print(i,end='')