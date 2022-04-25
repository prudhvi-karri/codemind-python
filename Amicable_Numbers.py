n=int(input())
m=int(input())
i=1
s1=0
while i<n:
    if n%i==0:
        s1=s1+i
    i=i+1
s2=0
j=1
while j<m:
    if m%j==0:
        s2=s2+j
    j=j+1
if s1==m and s2==n:
    print("Amicable")
else:
    print("Not Amicable")