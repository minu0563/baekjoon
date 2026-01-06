import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
num = list(map(int, input().split()))

# Prefix Sum 배열 계산
prefix_sum = [0] * (n + 1)
for i in range(1, n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + num[i - 1]

# 각 쿼리에 대해 부분 합 계산
for _ in range(m):
    l, r = map(int, input().split())
    result = prefix_sum[r] - prefix_sum[l - 1]
    print(result)
