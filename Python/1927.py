import heapq
import sys
input = lambda: sys.stdin.readline().rstrip()

l = []

for i in range(int(input())):
    a = int(input())

    if a != 0:
        heapq.heappush(l, a)
    elif a == 0:
        if not l:
            print(0)
        else:
            print(heapq.heappop(l)) #최솟값 출력