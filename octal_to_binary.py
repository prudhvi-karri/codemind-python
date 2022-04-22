b=int(input())
i=0
sum=0
while b!=0:
    d=b%10;
    sum=sum+(d)*(8**i)
    b=b//10;
    i=i+1;
print('{0:b}'.format(sum))