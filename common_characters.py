n=input().lower()
m=input().lower()
n=sorted(set(n))
s=''
for i in range(len(n)):
    if n[i] in m and n[i]!=' ':
        s+=n[i]
if len(s)==0:
    print(-1)
    exit()
print(s)