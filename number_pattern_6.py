#Code
n = int(input())

a,b = 1,1

while a <= n + 5:
    print(f"{a} "*b)
    a += 2
    b += 1

#Output
"""
5

1 
3 3 
5 5 5 
7 7 7 7 
9 9 9 9 9 
"""