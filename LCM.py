def hcf(a,b):
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    return a
a,b=map(int,input().split())
h=hcf(a,b)
print(a*b//h)