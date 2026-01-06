n, k = map(int, input().split())
l = sorted(list(map(int, input().split())), reverse= True)
l_1 = [i for i in range(1, n+1)]

for i in l:
    if i in l_1:
        l_1[l_1.index(i)] = 0

    elif i not in l_1:
        while True:
            i += k
            if i in l_1:
                l_1[l_1.index(i)] = 0
                break
            elif i > max(l_1):
                break

if l_1.count(0) == len(l_1):
    print(1)
else:
    print(0)