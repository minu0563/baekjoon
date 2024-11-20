from collections import deque
import sys
input = lambda: sys.stdin.readline().strip()

n = int(input())
l_1 = list(map(int, input().split()))
m = int(input())
l_2 = list(map(int, input().split()))

l_1.sort(reverse=True)
l_2.sort(reverse=True)

if l_2[0] > l_1[0]:
    print(-1)
    sys.exit()

time = 0
l_2 = deque(l_2)
num = 0
ans = 0

while l_2:
    for i in l_1:
        if not l_2:
            break
        if i >= l_2[0]:
            l_2.popleft()
        elif i >= min(l_2):
            while True:
                num += 1
                if i >= l_2[num]:
                    ans = l_2[num]
                    l_2.remove(ans)
                    num = 0
                    break
    time += 1
print(time)