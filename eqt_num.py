#Code
n = int(input())

for  i in range(1,n+1):
    print(" "*(n-i),end="")
    print(f"{i} "*i)

#Output
"""
8

       1 
      2 2 
     3 3 3 
    4 4 4 4 
   5 5 5 5 5 
  6 6 6 6 6 6 
 7 7 7 7 7 7 7 
8 8 8 8 8 8 8 8 
"""