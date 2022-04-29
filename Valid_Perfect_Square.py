l=1
a=int(input())
while l<=a:
    i=int(input())
    n=i**(1/2)
    if int(n)*n==i:
        print("True")
    else:
        print("False")
    l=l+1