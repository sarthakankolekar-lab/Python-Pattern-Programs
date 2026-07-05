#Code
n = int(input())

for i in range(n , 0 ,-1):
    for j in range(i):
        print(i,end=" ")
    print()

#Output
"""
5

5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1 
"""