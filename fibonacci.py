def fib(l):
    a,b=0,1
    if l==1:
        print(a)
    elif l==2:
        print(a,b)
    else:
        print(a,b,end=' ')
        for i in range(2,l):
            c=a+b
            print(c,end=' ')
            b,a=c,b
n=int(input())
fib(n)