#Code
n = int(input())

for i in range(1 , n + 1):
    print(" "*( (n * 2) - (i * 2) ),end="")
    for j in range(1 , i + 1):
        print(j,end=" ")
    print()

#Output
"""
5

        1 
      1 2 
    1 2 3 
  1 2 3 4 
1 2 3 4 5 
"""