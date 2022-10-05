n=input().split()
for i in n:
    l,k,m=[],[],[]
    for j in range(len(i)):
        if i[j].isalpha():
            m.append(i[j])
        else:
            l.append(j)
            k.append(i[j])
    m=sorted(m)
    v,o=0,0
    s=''
    for j in range(len(i)):
        if i[j].isalpha():
            s+=m[v]
            v+=1
        else:
            s+=k[o]
            o+=1
    print(s,end=' ')