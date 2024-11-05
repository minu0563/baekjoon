n, m = map(int, input().split())

l = []
for k in range(1, n+1):
    l += [k]

for _ in range(m):
    i, j = map(int, input().split())
    a = l[i-1]
    b = l[j-1]
    l[i-1] = b
    l[j-1] = a

print(*l)