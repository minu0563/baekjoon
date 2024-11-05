a, b = map(int,input().split())
c = []
for i in range(1, a+1):
    if a%i == 0:
        c.append(i)
        5
for _ in range(1):
    try:
        print(c[b-1])
    except IndexError:
        print(0)