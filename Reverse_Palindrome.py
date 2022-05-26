def is_pali(l):
    o=str(l)[::-1]
    if l==int(o):
        return 1
    else:
        return 0
n=int(input())
while 1:
    v=str(n)[::-1]
    m=n+int(v)
    if is_pali(m):
        print(m)
        break
    n=m