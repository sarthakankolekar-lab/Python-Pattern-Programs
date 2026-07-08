#Code
n = int(input())

for i in range(1,n+1):
    print(" "*2*(n-i),end="")
    for j in range(-i,i+1):
        if j == 0 or j == 1:
            continue
        elif j < 0:
            print(f"{j*-1} ",end="")
        else:
            print(f"{j} ",end="")
    print()

#Output
"""
9

                1 
              2 1 2 
            3 2 1 2 3 
          4 3 2 1 2 3 4 
        5 4 3 2 1 2 3 4 5 
      6 5 4 3 2 1 2 3 4 5 6 
    7 6 5 4 3 2 1 2 3 4 5 6 7 
  8 7 6 5 4 3 2 1 2 3 4 5 6 7 8 
9 8 7 6 5 4 3 2 1 2 3 4 5 6 7 8 9 
"""