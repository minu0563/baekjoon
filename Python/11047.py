import sys
input = lambda: sys.stdin.readline().rstrip()

a, b = map(int, input().split())
l = []
count = 0

for _ in range(a):
    c = int(input())
    l.append(c)

l = l[::-1]

for j in l:
    count += b//j
    b = b%j

print(count)