import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int , input().split())
l = list(map(int, input().split()))

st = 0
end = max(l)
ans = 0
while st <= end:
    mid = (st + end) // 2
    res = 0

    for i in l:
        if i > mid:
            res += i - mid

    if res >= m:
        ans = mid
        st = mid + 1
    else:
        end = mid - 1

print(ans)