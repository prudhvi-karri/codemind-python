a,b=map(int,input().split())
l=input().split()
s=0
for i in l:
    if len(str(abs(int(i))))==b:
        s+=1
print(s)