n=int(input())
k=list(map(str,input().split()))
p=[]
p=sorted(list(set(k)))
if(n>=3):
    print(p[-3])
else:
    print(max(k))