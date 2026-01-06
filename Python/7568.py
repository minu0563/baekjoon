a = int(input())
b = []
d = []

for i in range(a):
    b.append(list(map(int, input().split())))

for i in b:
    c = 1
    for j in b:
        if (j[0]>i[0])and(j[1]>i[1]):
            c += 1
    d.append(c)

print(*d, end = ' ')