def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
count = 0
l = []
l_2 = []

for _ in range(n):
    l.append(int(input()))

for i in range(n - 1):
    l_2.append(l[i+1] - l[i])

ans = l_2[0]
for i in range(1, len(l_2)):
    ans = gcd(ans, l_2[i])

for i in l_2:
    count += i // ans -1

print(count)