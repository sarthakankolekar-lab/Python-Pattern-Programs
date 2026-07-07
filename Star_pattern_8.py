#Code
n = int(input())

for i in range(n,n*-1,-1):
    if i > 0:
        print("* "*(n-i))
    else:
        print("* "*(n+i))

#Output
"""
5

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
* 
"""