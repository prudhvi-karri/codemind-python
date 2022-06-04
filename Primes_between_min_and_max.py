def is_prime(l):
    if l==1:
        return 0
    for i in range(2,int(l**0.5)+1):
        if l%i==0:
            return 0
    return 1
n=int(input())
l=list(map(int,input().split()))
t1=l.index(min(l))
t2=l.index(max(l))
c=0
if t2>=t1:
    for i in range(t1,t2+1):
        if is_prime(l[i]):
            c+=1
else:
    for i in range(t2,t1+1):
        if is_prime(l[i]):
            c+=1
print(c)