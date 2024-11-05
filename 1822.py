import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
l_1 = list(map(int, input().split()))
l_2 = set(map(int, input().split()))

l_3 = [i for i in l_1 if i not in l_2]
count = len(l_3)

if l_3:
    print(count)
    print(*sorted(l_3))

else:
    print(0)