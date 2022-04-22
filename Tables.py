a,b=map(int,input().split())
i=1
while i<=b:
    if i%2!=0:
        print('{0} x {1} = {2}'.format(a,i,a*i))
    i+=1