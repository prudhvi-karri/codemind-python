def is_pali(o):
    t=o
    rev=0
    while o!=0:
        r=o%10
        rev=rev*10+r
        o//=10
    if rev==t:
        return 1
    else:
        return 0
n=int(input())
for i in range(1,10000):
    if is_pali(n+i):
        m=n+i
        break
for i in range(1,10000):
    if is_pali(n-i):
        l=n-i
        break
if n-l==m-n:
    print(l,m)
elif n-l>m-n:
    print(m)
else:
    print(l)
    