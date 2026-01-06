a = int(input())
b = []
for i in range(a):
    x, y = map(int, input().split())
    b.append((x,y))
b.sort()

for n in b:
    print(n[0], n[1])