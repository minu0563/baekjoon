a, b = map(int, input().split())
l = [0]*a

for _ in range(b):
    i, j, k = map(int, input().split())
    for index in range(i-1, j):
        l[index] = k

print(*l)