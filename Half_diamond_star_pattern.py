a=int(input())
if a<3 or a>100:
    print('The pattern is not possible')
else:
    for i in range(1,a+1):
        for j in range(i):
            print('*',end="")
        print()
    for i in range(a-1,0,-1):
        for j in range(i):
            print('*',end="")
        print()