from collections import deque
import sys

input = lambda: sys.stdin.readline().rstrip()
l = deque()
count = 0

for i in range(int(input())):
    a = list(input().split())
    if len(a) == 1:
        a[0] = int(a[0])

    else:
        a[0] = int(a[0])
        a[1] = int(a[1])

    if a[0] == 1:
        l.appendleft(a[1])
        count += 1
    elif a[0] == 2:
        l.append(a[1])
        count += 1
    elif a[0] == 3:
        if l:
            print(l.popleft())
            count -= 1
        else:
            print(-1)
    elif a[0] == 4:
        if l:
            print(l.pop())
            count -= 1
        else:
            print(-1)
    elif a[0] == 5:
        print(count)
    elif a[0] == 6:
        if l:
            print(0)
        else:
            print(1)
    elif a[0] == 7:
        if l:
            print(l[0])
        else:
            print(-1)
    elif a[0] == 8:
        if l:
            print(l[-1])
        else:
            print(-1)