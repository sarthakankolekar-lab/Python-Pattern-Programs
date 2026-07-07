#Code
n = int(input())

for i in range(n):
    print("*"*(n-i),end="")
    print(" "*2*i,end="")
    print("*"*(n-i))

#Output
"""
8

****************
*******  *******
******    ******
*****      *****
****        ****
***          ***
**            **
*              *
"""