def is_pali(string):
    s=string[::-1]
    return 1 if s==string else 0
n=input().lower()
n=n.split()
c=0
for i in n:
    if is_pali(i):
        c+=1
print(c)