# 5 4 
# 1 2 3 4 5
# 2 1 3 4 5
# 2 1 4 3 5
# 3 4 1 2 5

a, b = map(int, input().split())
l = [i for i in range(1, a+1)]

for i in range(b):
    i, j = map(int, input().split())
    l[i-1:j] = l[i-1:j][::-1]


for i in l:
    print(i, end=' ')