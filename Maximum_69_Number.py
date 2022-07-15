n=input()
for i in range(len(n)):
    if n[i]=='6':
        n=n.replace("6","9",1)
        break
print(n)