def happy(k):
    if k<=9:
        return k
    else:
        s=0
        while k:
            s+=(k%10)*(k%10)
            k//=10
        return happy(s)
n=int(input())
v=happy(n)
if v==1 or v==7:
    print(True)
else:
    print(False)