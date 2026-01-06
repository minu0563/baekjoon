from collections import deque
import sys
lambda: sys.stdin.readline().rstrip()

l = deque()
ans = 0

for i in range(int(input())):
    a = list(input().split())

    if a[0] == 'push_front':
        l.appendleft(int(a[1]))
        ans += 1
    
    elif a[0] == 'push_back':
        l.append(int(a[1]))
        ans += 1
    
    elif a[0] == 'pop_front':
        if len(l) == 0:
            print(-1)
        else:
            print(l.popleft())
            ans -= 1
    
    elif a[0] == 'pop_back':
        if len(l) == 0:
            print(-1)
        else:
            print(l.pop())
            ans -= 1

    elif a[0] == 'size':
        print(ans)

    elif a[0] == 'empty':
        if ans == 0:
            print(1)
        else:
            print(0)

    elif a[0] == 'front':
        if l:
            print(l[0])
        else:
            print(-1)

    elif a[0] == 'back':
        if l:
            print(l[-1])
        else:
            print(-1)