def is_prime(l):
    if l==1:
        return 0
    for i in range(2,int(l**0.5)+1):
        if l%i==0:
            return 0
    return 1
a=int(input())
b=int(input())
c=a+b
i=1
while 1:
    if is_prime(c+i):
        t=c+i
        break
    i+=1
print(t-c)