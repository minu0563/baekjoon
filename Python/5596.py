a = list(map(int, input().split()))
b = list(map(int, input().split()))
s = 0
t = 0

for i in range(len(a)):
    s += a[i]
for x in range(len(b)):
    t += b[x]

if s > t:
    print(s)
elif s == t:
    print(s)
else:
    print(t)