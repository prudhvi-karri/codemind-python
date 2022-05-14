def is_prime(m):
    if m==0:
        return 0
    for j in range(2,int(m**(0.5))+1):
        if m%j==0:
            return 0
    return 1
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
        if is_prime(n+i):
            print(n+i)
            break