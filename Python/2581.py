import math

a = int(input())
b = int(input())
a = min(a,b)
b = max(a,b)
l = []

if a < 2:
    a = 2

array = [True for _ in range(b + 1)]
array[0] = array[1] = False

for i in range(2, int(math.sqrt(b)) + 1):
    if array[i]:
        for j in range(i*i, b+1, i):
            array[j] = False

for i in range(a, b+1):
    if array[i]:
        l.append(i)

if len(l) != 0:
    print(sum(l))
    print(min(l))
else:
    print(-1)