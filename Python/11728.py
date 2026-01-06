a, b = map(int, input().split())

l_1 = list(map(int, input().split()))
l_2 = list(map(int, input().split()))
l_3 = sorted(l_1+l_2)

for i in l_3:
    print(i, end=' ')