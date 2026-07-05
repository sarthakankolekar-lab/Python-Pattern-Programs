#Code
n = int(input())

a,b = 1,1

while a <= n:
    for i in range(a):
        print(b,end=" ")
        b += 1
    print()
    a += 1

#Output
"""
4

1 
2 3 
4 5 6 
7 8 9 10  
"""