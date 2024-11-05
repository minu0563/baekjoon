n,l,d = map(int, input().split())
time = 0
ans = 0

for i in range(n):
    time += l

    if time+5 > d and time+5 != d and time+5>d>time:
        ans = d
    else:
        time += 5

if ans != 0:
    print(ans)
else:
    print(n*l)