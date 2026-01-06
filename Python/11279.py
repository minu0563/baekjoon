import sys
import heapq
input = lambda: sys.stdin.readline().rstrip()
heap = []

for i in range(int(input())):
    a = int(input())

    if a > 0:
        heapq.heappush(heap, -a)
    elif a == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(-(heapq.heappop(heap)))