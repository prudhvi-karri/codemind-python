n=input().split()
s1,s2=0,0
for i in n:
    i=sorted(i)
    s1+=ord(i[0])
    s2+=ord(i[-1])
print(abs(s1-s2))