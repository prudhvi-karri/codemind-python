n=int(input())
a=[]
while n!=0:
    r=n%10
    a.append(r)
    n//=10
c,s=0,0
for i in range(len(a)):
    c=0
    for j in range(len(a)):
        if i!=j and a[i]==a[j]:
            c+=1
    if c==0:
        s+=1
if s==len(a):
    print("Unique Number")
else:
    print("Not Unique Number")