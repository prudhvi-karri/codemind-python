from math import sqrt
def is_prime(n):
    if n==1:
        return 0
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return 0
    return 1        
m=int(input())
c=0
for i in range(1,m+1):# 2 3 5 7 11 13
    if m%i==0:
        if is_prime(i)==0:
            c+=1
print(c)