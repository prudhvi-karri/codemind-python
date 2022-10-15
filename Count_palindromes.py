n=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
    temp = i  
    rev = 0  
    while(i > 0):  
        dig = i % 10  
        rev = rev * 10 + dig  
        i//=10
    if(temp == rev):  
        s+=1
print(s)