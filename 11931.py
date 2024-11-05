import sys
input = lambda: sys.stdin.readline().rstrip()
num = []

for _ in range(int(input())):
    num.append(int(input()))

num.sort(reverse=True)
for i in range(len(num)):
    print(num[i])