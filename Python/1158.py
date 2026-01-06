from collections import deque
n, k = map(int, input().split())
num = deque()

for i in range(1, n+1):
    num.append(i)

ans = []

while True:
    if len(num) == 0:
        break
    
    if len(num) != 0:
        for _ in range(k-1):
            nums = num.popleft()
            num.append(nums)
        ans.append(num.popleft())
    else:
        ans.append(num.popleft())

print(f"<{', '.join(map(str, ans))}>")