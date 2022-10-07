a,b=map(int,input().split())
if a==b+1 or b==a+1 or (a==1 and b==10) or (b==1 and a==10):
    print("Yes")
    exit()
print("No")