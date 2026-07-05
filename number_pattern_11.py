n = int(input())

for i in range(1 , n + 1):
    print(" "*( (n * 2) - (i * 2) ),end="")
    for j in range(1 , i + 1):
        print(j,end=" ")
    print()
