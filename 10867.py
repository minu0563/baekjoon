a = int(input())
num = list(map(int, input().split()))
num = list(set(num))
num.sort()

# for i in num:
#     print(i, end=' ')

print (*num)