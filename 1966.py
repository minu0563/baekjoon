a = int(input())

for _ in range(a):
    n, m = list(map(int, input().split()))
    queue = list(map(int, input().split()))
    queue = [(i, idx) for idx, i in enumerate(queue)]

    c = 0
    while True:
        if queue[0][0] == max(queue, key=lambda x:x[0])[0]:
            c += 1
            if queue[0][1] == m:
                print(c)
                break
            else:
                queue.pop(0)
        else:
            queue.append(queue.pop(0))