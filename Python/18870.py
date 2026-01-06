from bisect import bisect_left
import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
l = list(map(int, input().split()))
t = sorted(list(set(l)))

for i in l:
    print(bisect_left(t, i), end=' ')