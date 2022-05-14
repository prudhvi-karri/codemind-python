def is_prime(l):
    if l==1:
        return 0
    for i in range(2,int(l**(0.5)+1)):
        if l%i==0:
            return 0
    return 1
n=int(input())
for i in range(1,n+1):
    if is_prime(i)==1:
        if n%i==0 and is_prime(n/i)==1:
            print(i,n//i)
            break
else:
    print("-1")