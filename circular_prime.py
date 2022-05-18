def is_prime(l):
    if l==1:
        return 0
    for i in range(2,int(l**0.5)+1):
        if l%i==0:
            return 0
    return 1
n=int(input())
v=str(n)[::-1]
u=int(v)
if is_prime(n) and is_prime(u):
    print("circular prime")
elif is_prime(n)==0:
    print("not prime")
else:
    print("prime but not a circular prime")