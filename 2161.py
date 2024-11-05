from collections import deque
queue = deque()
num = []

for i in range(int(input()), 0, -1):
    queue.append(i)

while True:
    if len(queue) == 1:
        break
    else:
        num.append(queue[-1])
        queue.pop()
        right_value = queue.pop()
        queue.appendleft(right_value)

print(*num, queue[0])