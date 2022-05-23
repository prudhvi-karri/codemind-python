def is_prime(l):
    if l==1:
        return 0
    for i in range(2,int(l**0.5)+1):
        if l%i==0:
            return 0
    return 1
n=int(input())
m=int(input())
for i in range(n,m+1):
    if is_prime(i):
        print(i)