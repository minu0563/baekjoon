from collections import deque

queue = deque([i for i in range(1, int(input())+1)])

while True:
    if len(queue) != 1:
        queue.popleft()
        left = queue.popleft()
        queue.append(left)
    elif len(queue) == 1:
        print(queue.popleft())
        break