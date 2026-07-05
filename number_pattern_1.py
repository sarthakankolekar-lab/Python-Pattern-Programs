#Code
n = int(input())

for i in range(n+1):
    for j in range(i):
        print(i, end=" ")
    print()

#Output
"""
5

1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 
"""