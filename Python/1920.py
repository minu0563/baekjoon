import sys
input = sys.stdin.readline

num_1 = set()
num_2 = []

a = int(input())
num_1.update(map(int, input().split()))

b = int(input())
num_2.extend(map(int,input().split()))

for i in num_2:
    if i in num_1:
        print(1)
    else:
        print(0)