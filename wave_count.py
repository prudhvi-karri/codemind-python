n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(1,n-1):
    k=0
    if l[i-1]<l[i] and l[i]>l[i+1]:
        k=1
        c+=1
    if i%2 and k==0:
        print(-1)
        exit()
print(c)