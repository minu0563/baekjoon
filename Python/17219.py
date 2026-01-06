import sys
input = lambda: sys.stdin.readline().rstrip()

a, b = map(int, input().split())
l = {}

for i in range(a):
    dirc, key = input().split()
    l[dirc] = key

for _ in range(b):
    c = input()
    print(l[c])