def add(k):
    if k<=9:
        print(k)
    else:
        s=0
        while k:
            s+=(k%10)
            k//=10
        return add(s)
n=int(input())
add(n)