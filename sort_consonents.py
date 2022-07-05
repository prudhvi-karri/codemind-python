l=list(map(str,input().split()))
a='aeiou'
for i in range(len(l)):
    t=l[i]
    s=[]
    for j in range(len(t)):
        if t[j] not in a:
            s.append(t[j])
    s=sorted(s)
    n=0
    v=''
    for k in range(len(t)):
        if t[k] not in a:
            v+=s[n]
            n+=1
        else:
            v+=t[k]
    print(v,end=' ')