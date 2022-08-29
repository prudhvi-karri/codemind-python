def fib(k):
    l=[]
    l.append(0)
    l.append(1)
    for i in range(2,10000):
        l.append(l[i-1]+l[i-2])
        if l[i]>=k:
            if k-l[i-1]==l[i]-k:
                print(l[i-1],l[i])
                exit()
            elif k-l[i-1]<l[i]-k:
                print(l[i-1])
                exit()
            else:
                print(l[i])
                exit()
n=int(input())
fib(n)