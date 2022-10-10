n=int(input())
l=list(map(int,input().split()))
od,ev=0,0
for i in range(n):
    if i%2:
        od+=l[i]
    else:
        ev+=l[i]
print(abs(od-ev))