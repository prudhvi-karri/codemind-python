def is_prime(l):
    if l==1:
        return 0
    for i in range(2,int(l**(0.5))+1):
        if l%i==0:
            return 0
    return 1
n=int(input())
l=list(map(int,input().split()))
num=int(input())
s,k=0,0
for i in l:
    if is_prime(i) and i<=num:
        s+=1
print(s)