n=int(input())
m=n*n
a=[]
b=[]
while n!=0:
    r=n%10
    a.append(r)
    n//=10
while m!=0:
    r1=m%10
    b.append(r1)
    m//=10
c=0
for i in range(len(a)):
    if a[i] in b:
        c+=1
if c==len(a):
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')