from sys import stdin

n,k = map(int, stdin.readline().split())
a = 0
b = list(range(1, n+1))
c = []

while len(b) != 0:
    a += (k-1)
    a = a % len(b)
    c.append(b.pop(a))

print('<', end='')
for i in range(n-1):
    print(c[i], end=', ')
print(c[n-1], end='')
print('>',end='')