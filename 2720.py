a = [25, 10, 5, 1]
cnt = [0] * 4

for i in range(int(input())):
    b = int(input())
    for i in range(len(a)):
        cnt[i] = b // a[i]
        b -= a[i] * cnt[i]
    for k in range(len(cnt)):
        if k == 3 :
            print(cnt[k])
        else :
            print(cnt[k], end= ' ')