a = int(input())
l = list(map(int, input().split()))
l.sort()

b = 0
c = 0
for i in l:
    b += i
    c += b

print(c)