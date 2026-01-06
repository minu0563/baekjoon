n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = sorted(b)
d = 0
a.sort()

for i in range(n):
    d += a[-1]*c[0]
    del a[-1]
    del c[0]

print(d)