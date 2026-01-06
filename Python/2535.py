import sys
input = lambda: sys.stdin.readline().rstrip()

l = []
count = {}
ans = 0

for i in range(int(input())):
    l.append(list(map(int, input().split())))

l.sort(key= lambda x: x[2], reverse=True)

for i in range(len(l)):
    a, b, c = l[i]

    count[a] = count.get(a, 0) + 1

    if count[a] <= 2:
        print(a, b)
        ans += 1
    
    if ans == 3:
        break