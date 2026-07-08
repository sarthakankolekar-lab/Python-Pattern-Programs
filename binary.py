#Code
n = int(input())

for  i in range(1,n+1):
    for j in range(i):
        if (i-1) % 2 == 0:
            if j % 2 == 0:
                print("1 ",end="")
            else:
                print("0 ",end="")
        else:
            if j % 2 == 0:
                print("0 ",end="")
            else:
                print("1 ",end="")
    print()

#Output
"""
10

1 
0 1 
1 0 1 
0 1 0 1 
1 0 1 0 1 
0 1 0 1 0 1 
1 0 1 0 1 0 1 
0 1 0 1 0 1 0 1 
1 0 1 0 1 0 1 0 1 
0 1 0 1 0 1 0 1 0 1 
"""