n=list(map(str,input().lower().split()))
m=list(map(str,input().lower().split()))
for i in m:
    if i in n:
        print(i,end=' ')