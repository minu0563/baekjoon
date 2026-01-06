from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()

n,m = map(int, input().split())
num = list(map(int, input().split()))
dp = deque(i for i in range(1, n+1))

count = 0
for i in num:
    while True:
        if dp[0] == i:
            dp.popleft()
            break
        else:
            if dp.index(i) < len(dp)/2:
                dp.append(dp.popleft())
                count += 1
            else:
                dp.appendleft(dp.pop())
                count += 1

print(count)