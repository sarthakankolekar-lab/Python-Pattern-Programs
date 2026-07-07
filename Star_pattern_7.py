#Code
n = int(input())

for i in range(n+1):
    print("* "*i)

print()

for i in range(n,0,-1):
    print("* "*i)

#Output
"""
5

* 
* * 
* * * 
* * * * 
* * * * * 

* * * * * 
* * * * 
* * * 
* * 
* 
"""
