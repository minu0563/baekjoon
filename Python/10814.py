import sys
input = sys.stdin.readline

a = int(input())
b = []

for i in range(a):
    age , name  = input().split()
    age = int(age)
    b.append([age, i, name])
b.sort()

for x in b:
    print(x[0], x[2])