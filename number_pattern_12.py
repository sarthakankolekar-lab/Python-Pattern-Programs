#Code
n = int(input())

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j <= i:
            print(i, end=" ")
        else:
            print(j, end=" ")
    print()

#Output
"""
6

1 2 3 4 5 6 
2 2 3 4 5 6 
3 3 3 4 5 6 
4 4 4 4 5 6 
5 5 5 5 5 6 
6 6 6 6 6 6 
"""