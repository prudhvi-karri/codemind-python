n=input()
k=len(n)
n=int(n)
s,m=0,n
while n:
    d=n%10
    s+=d**k
    n//=10
    k-=1
if s==m:
    print(True)
else:
    print(False)