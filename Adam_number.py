n=int(input())
m=n*n#
t1=n
r1=0 #
while n!=0:
    re1=n%10
    r1=r1*10 + re1
    n=n//10
b=r1*r1
r2=0
while b!=0:
    re2=b%10
    r2=r2*10 +re2
    b=b//10
if m==r2:
    print("True")
else:
    print("False")
