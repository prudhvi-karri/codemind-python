a,b=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
c=0
for i in l2:
    if i not in l1:
        print("No")
        exit()
    l1.remove(i)
print("Yes")