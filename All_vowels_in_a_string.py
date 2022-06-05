n=input()
a='aeiou'
b=[]
for i in range(len(n)):
    if n[i] in a and n[i] not in b:
        b.append(n[i])
if len(b)==5:
    print(True)
else:
    print(False)