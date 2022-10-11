n=int(input())
l=list(map(int,input().split()))
s=0
for i in range(n):
    if i%2:
        s+=l[i]
print(s)