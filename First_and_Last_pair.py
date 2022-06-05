n=int(input())
l=list(map(int,input().split()))
j,k=0,n-1
s=[]
if n%2==1:
    for i in range(n//2+1):
        s.append(l[j])
        s.append(l[k])
        j+=1
        k-=1
    s[n]=0
else:
    for i in range(n//2):
        s.append(l[j])
        s.append(l[k])
        j+=1
        k-=1
print(*s)