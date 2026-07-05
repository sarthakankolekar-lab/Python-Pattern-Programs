#Code
n = int(input())

a = 1

for i in range(n , 0 , -1):
    for j in range(i):
        print(a , end=" ")
    a += 1
    print()

#Output
"""
5

1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
5
"""
