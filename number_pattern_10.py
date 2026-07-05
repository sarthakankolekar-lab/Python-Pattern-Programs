n = int(input())

a,b = 1,1

while a <= n:
    for i in range(a):
        print(b,end=" ")
        b += 1
    print()
    a += 1