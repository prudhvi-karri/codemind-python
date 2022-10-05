n=input()
l,m=[],[]
for i in range(len(n)):
    if n[i].isalpha():
        l.append(n[i])
    else:
        m.append(n[i])
l=sorted(l)
a,b,s=0,0,''
for i in range(len(n)):
    if n[i].isalpha():
        s+=l[a]
        a+=1
    else:
        s+=m[b]
        b+=1
print(s)