from math import gcd

for i in range(int(input())):
    ans = 0
    l = list(map(int, input().split()))
    for j in range(1, len(l)):
        for k in range(j+1, len(l)):
            ans += gcd(l[j], l[k])
    print(ans)
