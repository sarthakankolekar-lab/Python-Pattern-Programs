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
