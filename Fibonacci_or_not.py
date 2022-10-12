def fib(l):
    a,b=0,1
    for i in range(2,l):
        c=a+b
        if c==n:
            return True
        if c>n:
            return False
        b,a=c,b
n=int(input())
print(fib(n))