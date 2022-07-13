s=input()
s1=0
for i in range(len(s)):
    if s[i]=='U':
        s1+=1
    if s[i]=='D':
        s1+=-1
    if s[i]=='L':
        s1+=-1
    if s[i]=='R':
        s1+=1
if s1==0:
    print(True)
else:
    print(False)