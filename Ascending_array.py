n=int(input())
l=list(map(int,input().split()))
for i in range(1,n-1):
    if l[i+1]<=l[i]:
        print('no')
        exit()
print('yes')