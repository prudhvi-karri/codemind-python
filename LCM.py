def hcf(a,b):
    if b==0:
        return a
    else:
        return hcf(b,a%b)
n,m=map(int,input().split())
lcm=(n*m)//hcf(n,m)
print(int(lcm))