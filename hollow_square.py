#Code
n = int(input())

for  i in range(n):
    if i == 0 or i == n-1:
        print("* "*n)
    else:
        print("* ",end="")
        print(" "*2*(n-2),end="")
        print("* ")

#Output
"""
10

* * * * * * * * * * 
*                 * 
*                 * 
*                 * 
*                 * 
*                 * 
*                 * 
*                 * 
*                 * 
* * * * * * * * * *
"""