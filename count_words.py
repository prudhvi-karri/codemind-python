l=list(map(str,input().split()))
a=['a','e','i','o','u','A','E','I','O','U']
c=0
for i in range(len(l)):
    for j in range(len(l[i])):
        t=l[i]
        #print(t[0])
        if t[0] in a and t[len(l[i])-1] not in a:
            c+=1
            break
print(c)