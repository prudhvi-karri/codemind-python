x,y=map(int,input().split())
a=x+(y*2)
if x==0 and y%2!=0:
    print("NO")
elif a%2==0:
    print("YES")
else:
    print("NO")