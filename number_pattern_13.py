#Code
n = int(input())

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(f"{i*j}", end=" ")
    print()

#Output
"""
6

1
2 4
3 6 9
4 8 12 16
5 10 15 20 25
6 12 18 24 30 36
"""