from collections import deque
import sys
myqueue = deque()

for i in range(int(sys.stdin.readline())):
    a = sys.stdin.readline().strip().split()
    if a[0] == 'pop':
        if len(myqueue) != 0:
            print(myqueue.pop())
        else:
            print(-1)
    elif a[0] == 'push':
        myqueue.append(a[1])
    elif a[0] == 'size':
        print(len(myqueue))
    elif a[0] == 'empty':
        if len(myqueue) == 0:
            print(1)
        else:
            print(0)
    elif a[0] == 'top':
        if len(myqueue) != 0:
            print(myqueue[-1])
        else:
            print(-1)