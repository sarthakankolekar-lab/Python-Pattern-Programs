#Code
n = int(input())

mid = (n-1)/2
a = 1
b = int(mid)
c = 1

for i in range(1 , (n * 2) + 1 , 2):
    if i <= (mid * 2) + 1:
        print(" "*(n - i - b),"*"*i)
        b -= 1
    else:
        print(" "*((n - i + c) * -1),"*"*(i - (4 * a)))
        c += 1
        a += 1

#Output
"""
7

    *
   ***
  *****
 *******
  *****
   ***
    *
"""