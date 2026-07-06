#Code
n = int(input())

l = [1, 0]

for i in range(n):
    nl = []
    b, c = 0, 1
    if i == 0:
        print("1")
    else:
        print("1", end=" ")
        nl.append(1)
        for j in range(i):
            a = l[b] + l[c]
            print(a, end=" ")
            b += 1
            c += 1
            nl.append(a)
        nl.append(0)
        l = nl
        print()

#Output
"""
6

1
1 1 
1 2 1 
1 3 3 1 
1 4 6 4 1 
1 5 10 10 5 1
"""