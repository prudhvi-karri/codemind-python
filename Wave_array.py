n=int(input())
l=list(map(int,input().split()))
c,s=0,0
for i in range(0,n-1,2):
    if l[i]>l[i+1]:
        c+=1
    else:
        s+=1
if c==(n//2) or s==(n//2):
    print('yes')
else:
    print('no')